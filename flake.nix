{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
      mkPythonApp = {
        name,
        folder,
        main ? "main.py",
        packages ? _: [],
      }:
        pkgs.writeShellApplication {
          inherit name;
          runtimeInputs = [(pkgs.python3.withPackages packages)];
          text = ''
            python3 ${folder}/${main}
          '';
        };
    in {
      packages.project0 = mkPythonApp {
        name = "project0";
        folder = ./src;
        main = "project0.py";
        packages = pp: with pp; [numpy];
      };
    });
}
