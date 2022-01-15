
import unreal
from os import listdir
from os.path import isfile, join

package_path = "/Game/Items/Nuggets/Catalyzed/"
new_items_list = []

raw_files_path = package_path.replace("/Game/", "C:/Users/Alexandros/Desktop/astroneer_tinkering/pak/Astro/Content/")
onlyfiles = [f.replace(".uasset", "") for f in listdir(raw_files_path) if isfile(join(raw_files_path, f))]

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
factory = unreal.BlueprintFactory()
factory.set_editor_property("ParentClass", unreal.ItemType)

for f in onlyfiles:
    unreal.EditorAssetLibrary.save_loaded_asset(asset_tools.create_asset(f, package_path, None, factory))
    
"""
import unreal
from shutil import copyfile
from os import listdir
from os.path import isfile, join
package_path = "/Game/UI/Textures/Icons/Packages"
new_items_list = []

raw_files_path = package_path.replace("/Game/", "C:/Users/Alexandros/Desktop/astroneer_tinkering/pak/Astro/Content/")
onlyfiles = [f.replace(".uasset", "") for f in listdir(raw_files_path) if isfile(join(raw_files_path, f))]

asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
factory = unreal.TextureFactory()
factory.set_editor_property("SupportedClass", unreal.Texture2D)

for f in onlyfiles:
    task = unreal.AutomatedAssetImportData()
    task.replace_existing = True
    task.factory = factory
    task.destination_path = package_path
    task.filenames = ["C:\\Users\\Alexandros\\Desktop\\um\\tmp\\" + f + ".tga"]
    copyfile("C:\\Users\\Alexandros\\Desktop\\um\\tmp\\blank_white_pixel.tga", task.filenames[0])
    unreal.EditorAssetLibrary.save_loaded_asset(asset_tools.import_assets_automated(task)[0])"""