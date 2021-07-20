# script to automatically produce reports for google bucket access
import papermill as pm

# workspace="DepMap_Mutation_Calling_CGA_pipeline/CCLF_TSCA_2_0_2"
# workspace="nci-mimoun-bi-org/CCLF_WES"
workspace="terra-broad-cancer-prod/CCLF_Bass_GE_ModelCharacterization"
pathto_input = "./check_gs_path_access.ipynb"
pathto_output = "./results/check_bucket_reports/Access_Report_"+workspace.replace("/", "-")+".ipynb"

pm.execute_notebook(
   pathto_input,
   pathto_output,
   parameters = dict(workspace=workspace)
)
