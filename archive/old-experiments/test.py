from tree_sitter import Language, Parser
import tree_sitter_c as tsc
import re

# Initialize the C language using tree_sitter_c
tsc.language()  # ensure the language is loaded
C_LANGUAGE = Language(tsc.language())
c_parser = Parser(C_LANGUAGE)

def get_relevant_cutoff(source_code: str, patch_start_line: int, patch_end_line: int) -> str:
    """
    Given C source code and patch boundaries (1-indexed),
    returns a snippet that includes complete function definitions overlapping
    the patch. If the patch falls inside a function, the snippet is extended to
    include the entire function.
    """
    # Split source code into lines
    lines = source_code.splitlines()
    patch_start_idx = patch_start_line - 1  # convert to 0-indexed
    patch_end_idx = patch_end_line - 1

    # Parse the source code using the custom C parser
    tree = c_parser.parse(source_code.encode('utf8'))
    root = tree.root_node

    # Set initial boundaries to the given patch
    new_start = patch_start_idx
    new_end = patch_end_idx

    def traverse(node):
        yield node
        for child in node.children:
            yield from traverse(child)

    # Traverse the tree and extend the boundaries if the patch falls inside a function
    for node in traverse(root):
        if node.type == 'function_definition':
            func_start = node.start_point[0]
            func_end = node.end_point[0]
            # If function overlaps with the patch region, adjust the boundaries
            if func_start <= patch_end_idx and func_end >= patch_start_idx:
                new_start = min(new_start, func_start)
                new_end = max(new_end, func_end)

    # Return the snippet that covers the adjusted boundaries
    snippet = "\n".join(lines[new_start:new_end+1])
    return snippet


def print_code_with_line_numbers(code_str: str):
    """
    Utility function to print the code along with line numbers.
    """
    lines = code_str.splitlines()
    for i, line in enumerate(lines, start=1):
        print(f"{i:3d}: {line}")


c_code = """
#include <stdio.h>

void foo() {
    printf("This is foo\\n");
}

void bar() {
    printf("This is bar\\n");
    // The patch might modify this line
    printf("Modified line\\n");
}

#define MIN 10000

int main() {
    foo();
    bar();
    return 0;
}
""".strip()

# Suppose the patch touches line 10 (1-indexed) which is within 'bar'
patch_start = 10
patch_end = 15



print("=== Original Code with Line Numbers ===")
print_code_with_line_numbers(c_code)

snippet = get_relevant_cutoff(c_code, patch_start, patch_end)

print("\n=== Extracted Snippet with Line Numbers ===")
print_code_with_line_numbers(snippet)

patterns = {
    "if_else_block": "(if_statement) @if_block",
    "return_statement": "(return_statement) @return_stmt",
    "switch_block": "(switch_statement) @switch_block",
    "memory_allocation": """
      (call_expression 
         function: (identifier) @mem_func
      ) (#match? @mem_func "^(malloc|calloc|realloc|free)$")
    """,
    "standard_io": """
      (call_expression 
         function: (identifier) @io_func
      ) (#match? @io_func "^(printf|sprintf)$")
    """,
    "conversion_functions": """
      (call_expression 
         function: (identifier) @conv_func
      ) (#match? @conv_func "^(atof|atoi|atol|atoll)$")
    """,
    "standard_library_functions": """
      (call_expression 
         function: (identifier) @lib_func
      ) (#match? @lib_func "^(bsearch|qsort|time|date|memcmp|memcpy|memmove)$")
    """,
    "locale_env_functions": """
      (call_expression 
         function: (identifier) @locale_func
      ) (#match? @locale_func "^(localeconv|getenv|setlocale|strerror|asctime|ctime|gmtime|localtime)$")
    """,
    "random_number_functions": """
      (call_expression 
         function: (identifier) @rand_func
      ) (#match? @rand_func "^(rand|srand)$")
    """,
    "function_parameters": "(parameter_list) @params",
    "union_usage": "(union_specifier) @union_usage",
    "undef_directive": "(preproc_call) @undef_directive (#match? @undef_directive \"^#undef\")",
    "preprocessor_conditionals": "(preproc_call) @preproc_cond (#match? @preproc_cond \"^#(if|ifdef|ifndef|elif|else|endif)\")",
    "goto_statement": "(goto_statement) @goto_stmt",
    "break_statement": "(break_statement) @break_stmt",
    "data_types": """
      ((type_identifier) @type_id (#match? @type_id "^(int|float|short|unsigned|double|char|long)$"))
    """,
    "pointer_usage": "(pointer_declarator) @pointer_usage",
}


def extract_from_c_code(code: str) -> dict:
    # Initialize results dictionary using the keys in patterns.
    results = {key: [] for key in patterns}
    # Process inline and recursive functions separately.
    results["inline_function"] = []
    results["recursive_function"] = []

    code_bytes = code.encode("utf8")
    parser = Parser(C_LANGUAGE)
    tree = parser.parse(code_bytes)
    root_node = tree.root_node

    # Process each pattern.
    for classification, query_str in patterns.items():
        query = C_LANGUAGE.query(query_str)
        # Group the captures by their capture names.
        for node_list in query.captures(root_node).values():
            for node in node_list:
                # node.start_point and node.end_point are [row, column]
                extracted_text = code_bytes[node.start_byte:node.end_byte].decode("utf8").strip()
                results[classification].append({
                    "classification": classification,
                    "extracted_line": extracted_text,
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1
                })

    query_inline = C_LANGUAGE.query("(function_definition) @func_def")
    for node_list in query_inline.captures(root_node).values():
        for node in node_list:
            func_text = code_bytes[node.start_byte:node.end_byte].decode("utf8")
            # Use regex to check if the function starts with 'inline'
            if re.match(r'^\s*inline\b', func_text):
                results["inline_function"].append({
                    "classification": "inline_function",
                    "extracted_line": func_text.strip(),
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1
                })

    # =============================================================================
    # Process recursive functions:
    # =============================================================================
    query_func_def = C_LANGUAGE.query("(function_definition) @func_def")
    def find_identifier(n):
        # Recursively search for a node of type "identifier" within n.
        if n.type == "identifier":
            return code_bytes[n.start_byte:n.end_byte].decode("utf8")
        for child in n.children:
            res = find_identifier(child)
            if res:
                return res
        return None

    # captures_func_def = query_func_def.captures(root_node)
    for node_list in query_func_def.captures(root_node).values():
        for node in node_list:
            func_name = find_identifier(node)
            if not func_name:
                continue
            # Locate the function's compound statement.
            body_text = ""
            for child in node.children:
                if child.type == "compound_statement":
                    body_text = code_bytes[child.start_byte:child.end_byte].decode("utf8")
                    break
            # Check if the function calls itself.
            if body_text and re.search(r'\b' + re.escape(func_name) + r'\s*\(', body_text):
                func_text = code_bytes[node.start_byte:node.end_byte].decode("utf8")
                results["recursive_function"].append({
                    "classification": "recursive_function",
                    "extracted_line": func_text.strip(),
                    "start_line": node.start_point[0] + 1,
                    "end_line": node.end_point[0] + 1
                })

    return results

sample_code = r"""
#include <stdio.h>
#include <stdlib.h>

#define MAX 100

inline int add(int a, int b) {
    return a + b;
}

int32_t factorial(int n) {
    if(n <= 1)
        return 1;
    else
        return n * factorial(n - 1);
}

void *my_malloc(size_t size) {
    return malloc(size);
}

int main() {
    int x = 10;
    if(x > 0) {
        printf("Positive\n");
    } else {
        printf("Non-positive\n");
    }
    switch(x) {
        case 10:
            break;
        default:
            break;
    }
    goto end;
    end:
    return 0;
}
"""

extracted = extract_from_c_code(sample_code)
# For pretty printing the results:
import json
print(json.dumps(extracted, indent=2))


def find_identifier(node, code_bytes):
    """
    Recursively search for an "identifier" node inside the given node.
    Returns the decoded identifier text or None if not found.
    """
    if node.type == "identifier":
        return code_bytes[node.start_byte:node.end_byte].decode("utf8")
    for child in node.children:
        identifier = find_identifier(child, code_bytes)
        if identifier:
            return identifier
    return None

def get_function_boundaries(code: str) -> list:
    """
    Extracts all function boundaries from the provided C code.
    
    Returns a list of dictionaries where each dictionary contains:
      - function_name: Name of the function.
      - start_line: The starting line (1-indexed) of the function definition.
      - end_line: The ending line (1-indexed) of the function definition.
    """
    code_bytes = code.encode("utf8")
    parser = Parser(C_LANGUAGE)
    tree = parser.parse(code_bytes)
    root_node = tree.root_node

    # Query for function_definition nodes.
    query = C_LANGUAGE.query("(function_definition) @func_def")
    boundaries = []
    for node_list in query.captures(root_node).values():
        for node in node_list:
            func_name = find_identifier(node, code_bytes)
            if not func_name:
                continue
            start_line = node.start_point[0] + 1  # tree-sitter rows are 0-indexed
            end_line = node.end_point[0] + 1
            boundaries.append({
                "function_name": func_name,
                "start_line": start_line,
                "end_line": end_line
            })
    return boundaries

def get_c_code_boundaries(code: str) -> dict:
    """
    Returns the boundaries of the entire C code as a dictionary with:
      - start_line: The first line (1-indexed).
      - end_line: The last line (1-indexed).
      
    This is determined by the root node's start and end positions.
    """
    code_bytes = code.encode("utf8")
    parser = Parser(C_LANGUAGE)
    tree = parser.parse(code_bytes)
    root_node = tree.root_node
    return {
        "start_line": root_node.start_point[0] + 1,
        "end_line": root_node.end_point[0] + 1
    }


if __name__ == "__main__":
    sample_code = r"""
    I am writing this c code
    return x * x;
    to find the boundary. lets
    find it lol

    #include <stdio.h>
    #include <stdlib.h>

    inline int square(int x) {
        return x * x;
    }

    int factorial(int n) {
        if (n <= 1)
            return 1;
        else
            return n * factorial(n - 1);
    }

    int main() {
        int x = 10;
        printf("Hello, World!\n");
        return 0;
    }

    this should not be counted lol
    """
    
    print("Function Boundaries:")
    functions = get_function_boundaries(sample_code)
    for func in functions:
        print(func)
    
    print("\nC Code Boundaries:")
    code_bounds = get_c_code_boundaries(sample_code)
    print(code_bounds)