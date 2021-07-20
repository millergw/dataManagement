# dataManagement

Use the `check_gs_path_access.ipynb` to do a comprehensive check of all the Google storage paths that exist in the workspace. All you need to provide is the workspace name. The elements checked include:
- tables
- workspace data
- workflow inputs and outputs

This notebook requires the JKBio repo, and various python libraries including dalmation.

The `automate_check_bucket_report.py` file allows for automatic generation of access reports using papermill.
