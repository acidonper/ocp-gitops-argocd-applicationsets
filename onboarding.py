# import pyyaml module
import yaml
from yaml.loader import SafeLoader
import glob

def folderTreeExtract(servicesPath):
    folders = glob.glob(servicesPath)
    files = {}
    for folder in folders: 
        files[folder] = []
        valuesfiles = glob.glob(folder + "/apps/*/*.yaml")
        for valuesFile in valuesfiles:
          files[folder].append(valuesFile)
    return files

def applicationDefinition(tree):
    for folder in tree:
        name = folder.split("/")[-1]
        with open('argocd/Application_tmpl.yaml') as f:
            data = yaml.load(f, Loader=SafeLoader)
            data['metadata']['name'] = name
            data['spec']['source']['helm']['valueFiles'] = tree[folder]
            data['spec']['destination']['namespace'] = name
        with open('argocd/applications/' + name + '.yaml', 'w') as d:
            destination = yaml.dump(data, d, sort_keys=False, default_flow_style=False)

def main():
    tree = folderTreeExtract("./onboarding/*")
    applicationDefinition(tree)

if __name__ == '__main__':
    main()