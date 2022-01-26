cmake_minimum_required(VERSION 3.13.4)

project(LanguagePacks)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/Slicer/SlicerLanguagePacks")
set(EXTENSION_CATEGORY "Utilities")
set(EXTENSION_CONTRIBUTORS "Andras Lasso (PerkLab)")
set(EXTENSION_DESCRIPTION "Extension for deploying language packs and editing translations.")
# Icon source: https://freesvg.org/united-globe. License: Public Domain.
set(EXTENSION_ICONURL "https://raw.githubusercontent.com/Slicer/SlicerLanguagePacks/main/LanguagePacks.png")
set(EXTENSION_SCREENSHOTURLS "https://raw.githubusercontent.com/Slicer/SlicerLanguagePacks/main/Docs/LanguageSelector.png https://raw.githubusercontent.com/Slicer/SlicerLanguagePacks/main/Docs/ExampleTranslations.png https://raw.githubusercontent.com/Slicer/SlicerLanguagePacks/main/Docs/LanguageTools.png")
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
