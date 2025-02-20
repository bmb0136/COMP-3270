{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
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
      packages.default = self.packages.${system}.project2;
      packages.project0 = mkPythonApp {
        name = "project0";
        folder = ./src;
        main = "project0.py";
        packages = pp: with pp; [numpy];
      };
      packages.project1 = mkPythonApp {
        name = "project1";
        folder = ./src;
        main = "project1.py";
        packages = pp: [];
      };
      packages.project2 = mkPythonApp {
        name = "project2";
        folder = ./src;
        main = "project2.py";
        packages = pp: with pp; [matplotlib];
      };
    });
}
