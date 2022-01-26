cmake_minimum_required(VERSION 3.13.4)

project(LanguagePacks)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://www.slicer.org/wiki/Documentation/Nightly/Extensions/LanguagePacks")
set(EXTENSION_CATEGORY "Utilities")
set(EXTENSION_CONTRIBUTORS "Andras Lasso (PerkLab)")
set(EXTENSION_DESCRIPTION "Extension for deploying language packs and editing translations.")
set(EXTENSION_ICONURL "http://www.example.com/Slicer/Extensions/LanguagePacks.png")
set(EXTENSION_SCREENSHOTURLS "http://www.example.com/Slicer/Extensions/LanguagePacks/Screenshots/1.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(LanguageTools)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
