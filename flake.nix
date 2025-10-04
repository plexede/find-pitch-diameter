{
  "description": "Nix flake for a PyQt6 development environment",
  "inputs": {
    "nixpkgs": {
      "url": "github:NixOS/nixpkgs",
      "inputs": {
        "flake-compat": {
          "url": "github:numtide/flake-compat"
        }
      }
    }
  },
  "outputs": {
    "devShell": {
      "default": {
        "packages": [
          "nixpkgs.python310Packages.pyqt6"
        ]
      }
    }
  }
}