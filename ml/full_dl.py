import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader


class MLPClassifier(nn.Module):
    def __init__(self, d_in, hidden, n_classes):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(d_in, hidden),
            nn.ReLU(),
            nn.Linear(hidden, n_classes)
        )

    def forward(self, X):
        # X: (B, d)
        # output: (B, C)
        return self.net(X)


def evaluate(model, loader, criterion, device):
    model.eval()

    total_loss = 0.0
    total_correct = 0
    total_examples = 0

    with torch.no_grad():
        for X, y in loader:
            X = X.to(device)       # (B, d)
            y = y.to(device)       # (B,)

            logits = model(X)      # (B, C)
            loss = criterion(logits, y)

            # Sum batch-average loss correctly
            total_loss += loss.item() * X.size(0)

            pred = logits.argmax(dim=1)   # (B,)
            total_correct += (pred == y).sum().item()
            total_examples += y.size(0)

    avg_loss = total_loss / total_examples
    accuracy = total_correct / total_examples

    return avg_loss, accuracy


def train_model(
    model,
    train_loader,
    val_loader,
    epochs=10,
    lr=1e-3,
    device="cpu"
):
    model = model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()

        total_train_loss = 0.0
        total_examples = 0

        for X, y in train_loader:
            X = X.to(device)       # (B, d)
            y = y.to(device)       # (B,)

            optimizer.zero_grad()

            logits = model(X)      # (B, C)
            loss = criterion(logits, y)

            loss.backward()
            optimizer.step()

            total_train_loss += loss.item() * X.size(0)
            total_examples += X.size(0)

        train_loss = total_train_loss / total_examples

        val_loss, val_acc = evaluate(
            model, val_loader, criterion, device
        )

        print(
            f"Epoch {epoch + 1}: "
            f"train_loss={train_loss:.4f}, "
            f"val_loss={val_loss:.4f}, "
            f"val_acc={val_acc:.4f}"
        )

    return model


X_train = torch.randn(1000, 20)
y_train = torch.randint(0, 3, (1000,))

X_val = torch.randn(200, 20)
y_val = torch.randint(0, 3, (200,))

train_ds = TensorDataset(X_train, y_train)
val_ds = TensorDataset(X_val, y_val)

train_loader = DataLoader(
    train_ds,
    batch_size=32,
    shuffle=True
)

val_loader = DataLoader(
    val_ds,
    batch_size=64,
    shuffle=False
)

device = "cuda" if torch.cuda.is_available() else "cpu"

model = MLPClassifier(
    d_in=20,
    hidden=64,
    n_classes=3
)

model = train_model(
    model,
    train_loader,
    val_loader,
    epochs=10,
    lr=1e-3,
    device=device
)

test_loss, test_acc = evaluate(
    model,
    test_loader,
    criterion,
    device
)