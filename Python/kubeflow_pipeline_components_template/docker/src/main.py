import logging # for printing to console at kubeflow pipeline
import argparse # for parsing arguments

def parse_arguments():
    parser = argparse.ArgumentParser(description="Some Description")
    parser.add_argument(
        "--variable-name",
        type="some_type",
        help="some description on the variable name"
    )
    # add all arguemnts
    #output path
    parser.add_argument(
        "--output",
        type="output type",
        help="output description"
    )
    args = parser.parse_args(args=args)
    return args

def main():
    logging.basicConfig(level=logging.INFO)
    args = parse_arguments()

    ## ENTER SOME CODE HERE
     


if __name__ == "__main__":
    main()