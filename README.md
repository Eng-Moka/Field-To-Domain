# ArcGIS Field to Domain Converter

This Python script automates the process of converting fields in a specified layer into domains within the ArcGIS environment. It is particularly useful for managing data integrity and enforcing data validation rules.

## Overview

This script is designed to be executed within ArcGIS Pro. It performs the following key steps:

1. **Get GDB Path of Layer**: Obtains the path of the geodatabase (GDB) containing the specified layer.
2. **Field-To-Domain Function**: Main function `Field-To-Domain` that accepts parameters for the feature class (fc), field, and domain name.
3. **Check Domain Existence**: Checks if the domain with the specified name already exists in the geodatabase.
4. **Determine Field Type**: Determines the type of the specified field.
5. **Create Domain**: Creates a new domain based on the field type if it doesn't already exist.
6. **Retrieve Unique Field Values**: Retrieves unique values from the specified field.
7. **Add Coded Values to Domain**: Adds unique field values as coded values to the domain.
8. **Assign Domain to Field**: Assigns the created domain to the specified field.
9. **Update Field Values**: Updates existing field values with corresponding domain code values.
10. **Script Execution**: Executes the `Field-To-Domain` function with provided parameters.

![1](https://github.com/Eng-Moka/Field-To-Domain/assets/132586649/c0e815e3-803d-4fa9-9212-fd0d09305780)

![2](https://github.com/Eng-Moka/Field-To-Domain/assets/132586649/92c4f141-dc46-44b4-b416-ce1da9024f54)

![3](https://github.com/Eng-Moka/Field-To-Domain/assets/132586649/11faf0c7-26e5-4695-96de-15698a39d94e)


## Additional Notes

- Ensure that ArcGIS Pro is installed and configured properly on your system.
- This script relies on the arcpy module provided by ArcGIS, hence it should be executed within an ArcGIS environment.
- Make sure to have appropriate permissions to access the specified geodatabase and modify domains.
- The script assumes that the input parameters provided are valid and exist within the ArcGIS environment.

Feel free to modify the script or customize it further to suit your specific requirements or workflow.

