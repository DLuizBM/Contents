from importlib import metadata

# metadata serve para verificar dados internos

print(metadata.version('pip'))

metadata_pip = metadata.metadata('pip')
print(list(metadata_pip))
print(metadata_pip)
print(metadata_pip['Project-URL'])