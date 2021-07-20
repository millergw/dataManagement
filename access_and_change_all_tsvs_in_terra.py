import pandas as pd

def accessAndChange(func, wmfrom, wmto=None):
  data = {}
  try:
    a = wmfrom.get_participants()
    data.update({'participants': a})
  except:
    print('no participants')
  try:
    a = wmfrom.get_samples()
    data.update({'samples': a})
  except:
    print('no samples')
  try:
    a = wmfrom.get_pair_sets()
    data.update({'pair_sets': a})
  except:
    print('no pair_sets')
  try:
    a = wmfrom.get_pairs()
    data.update({'pairs': a})
  except:
    print('no pairs')
  try:
    a = wmfrom.get_sample_sets()
    data.update({'sample_sets': a})
  except:
    print('no sample_sets')
  # currently works only for sample, sample
  for key, entity in data.iteritems():
      data[key] = func(key,entity)
  if wmto is None:
    wmto = wmfrom
  if "participants" in data:
    wmto.upload_participants(data['participants'])
  if "samples" in data:
    wmto.upload_samples(data['samples'])
  if "pairs" in data:
    wmto.upload_pairs(data['pairs'])
  if "pair_set" in data:
    pairset = data['pair_set'].drop('pairs', 1)
    wmto.upload_entities('pair_set', pairset)
    for i, val in data['pair_set'].iterrows():
      wmto.update_pair_set(i, val.pairs)
  if "sample_set" in data:
    sampleset = data['sample_set'].drop('samples', 1)
    wmto.upload_entities('sample_set', sampleset)
    for i, val in data['sample_set'].iterrows():
      wmto.update_sample_set(i, val.samples)


# func(key, entity) where entity is a tsv (e.g. sample_set.tsv or sample_set tsv from Tera)
# and key is the string name of that tsv (e.g. "sample_set")

def switch_dfs_with_local_files(wmfrom,pathto_new_folder, wmto=None):
  '''
  use this function if you have a new versions of the dfs/entities already made
  and stored in a folder (path given by pathto_new_folder)
  (e.g. made using an R script and saved to file)
  only requirement is that the new df's file name matches the name of the entity in Terra (e.g. must be sample_set, not sampleSet or sampleSets etc.)!
  '''
  data = {}
  try:
    a = wmfrom.get_participants()
    data.update({'participant': a})
  except:
    print('no participants')
  try:
    a = wmfrom.get_samples()
    data.update({'sample': a})
  except:
    print('no samples')
  try:
    a = wmfrom.get_pair_sets()
    data.update({'pair_set_entity': a})
  except:
    print('no pair_sets')
  try:
    a = wmfrom.get_pairs()
    data.update({'pair': a})
  except:
    print('no pairs')
  try:
    a = wmfrom.get_sample_sets()
    data.update({'sample_set_entity': a})
  except:
    print('no sample_sets')
  # currently works only for sample, sample
  for key, entity in iter(data.items()):
      pathto_new_entity = pathto_new_folder + key + '.tsv'
      print(pathto_new_entity)
      data[key] = pd.read_csv(pathto_new_entity, sep='\t') # func(key,entity)
  return data
  if wmto is None:
    wmto = wmfrom
  if "participants" in data:
    wmto.upload_participants(data['participants'])
  if "samples" in data:
    wmto.upload_samples(data['samples'])
  if "pairs" in data:
    wmto.upload_pairs(data['pairs'])
  if "pair_set" in data:
    pairset = data['pair_set'].drop('pairs', 1)
    wmto.upload_entities('pair_set', pairset)
    for i, val in data['pair_set'].iterrows():
      wmto.update_pair_set(i, val.pairs)
  if "sample_set" in data:
    sampleset = data['sample_set'].drop('samples', 1)
    wmto.upload_entities('sample_set', sampleset)
    for i, val in data['sample_set'].iterrows():
      wmto.update_sample_set(i, val.samples)
