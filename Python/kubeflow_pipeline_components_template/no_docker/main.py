from kfp.components import create_component_from_func, OutputPath

def main(
    some_value: some_type,
    output_path: OutputPath(),
):
    # enter some code here
    pass

#{VERSION} should be appropriate
#whatever non-standard packages to be installed must be within packages_to_install
if __name__ == "__main__":
    create_component_from_func(
        main,
        output_component_file="component.yaml",
        base_image="python:{VERSION}",
        packages_to_install=[],
    )
