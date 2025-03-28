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
            pushd ${folder} >/dev/null 2>/dev/null
            python3 ${main} "$@"
            popd >/dev/null 2>/dev/null
          '';
        };
    in {
      packages.default = self.packages.${system}.project3;
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
      packages.project3 = mkPythonApp {
        name = "project3";
        folder = ./src/project3;
        main = "homework3.py --graph ${./src/project3/graph.pickle}";
        packages = pp: with pp; [networkx matplotlib];
      };
    });
}
