// complex_segfault.cpp
#include <iostream>
#include <cstdlib>
#include <cstring>

void invalidFree()
{
    // Allocate 10 bytes on the heap
    char* buf = (char*)std::malloc(10);
    std::memset(buf, 'A', 10);

    // Create a “wrong” pointer that points 5 bytes into the block
    char* ptr = buf + 5;
    std::cout << "Freeing wrong pointer: " << static_cast<void*>(ptr) << std::endl;

    // This will invoke undefined behavior—on most libc implementations it raises
    // SIGSEGV because free() tries to read metadata just before 'ptr'
    std::free(ptr);
}

int main()
{
    std::cout << "Starting complex segfault example...\n";
    invalidFree();
    // We never get here
    return 0;
}
