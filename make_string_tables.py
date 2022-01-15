import unreal
from os import listdir
from os.path import isfile, join

package_path = "/Game/Globals/StringTables"
new_items_list = []

raw_files_path = package_path.replace("/Game/", "C:/Users/Alexandros/Desktop/astroneer_tinkering/pak/Astro/Content/")
onlyfiles = [f.replace(".uasset", "") for f in listdir(raw_files_path) if isfile(join(raw_files_path, f))]

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
factory = unreal.StringTableFactory()

for f in onlyfiles:
    my_new_asset = asset_tools.create_asset(f, package_path, None, factory)
    unreal.EditorAssetLibrary.save_loaded_asset(my_new_asset)