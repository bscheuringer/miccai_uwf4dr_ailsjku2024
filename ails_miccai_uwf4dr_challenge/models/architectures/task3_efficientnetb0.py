import torch
import torch.nn as nn
from efficientnet_pytorch import EfficientNet
from pathlib import Path

class Task3EfficientNetB0(nn.Module):
    def __init__(self, num_classes=1):
        super(Task3EfficientNetB0, self).__init__()
        self.num_classes = num_classes
        # Get model and replace the last layer
        self.model = EfficientNet.from_pretrained('efficientnet-b0', num_classes=num_classes)

        self.loss_fn = nn.BCEWithLogitsLoss()

    def forward(self, x):
        return self.model(x)
    
    def predict(self, x):
        with torch.no_grad():
            if self.num_classes > 1:
                pred = torch.softmax(self(x), dim=1)[0][-1]
            else:
                pred = torch.sigmoid(self(x))
        return pred

def main():
    # Initialize model, criterion, optimizer
<<<<<<< HEAD
    model = Task2EfficientNetB0(num_classes=1)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    x = torch.randn(1, 3, 800, 1016).to(device)
=======
    model = Task3EfficientNetB0(num_classes=1)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    x = torch.randn(1, 3, 512, 512).to(device)
>>>>>>> d7caa81 (cv should work)
    y_hat = model.predict(x).item()
    print(y_hat)

if __name__ == "__main__":
    main()
