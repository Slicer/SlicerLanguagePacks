Glossary

Terms used in various fields of medical and biomedical image computing and clinical images are not always consistent. This section defines terms that are commonly used in 3D Slicer, especially those that may have different meaning in other contexts.

Bounds: Describes bounding box of a spatial object along 3 axes. Defined in VTK by 6 floating-point values: X_min, X_max, Y_min, Y_max, Z_min, Z_max.

Brightness/contrast: Specifies linear mapping of voxel values to brightness of a displayed pixel. Brightness is the linear offset, contrast is the multiplier. In medical imaging, this linear mapping is more commonly specified by window/level values.

Cell: Data cells are simple topological elements of meshes, such as lines, polygons, tetrahedra, etc.

Color legend (or color bar, scalar bar): a widget overlaid on slice or 3D views that displays a color legend, indicating meaning of colors.

Coordinate system (or coordinate frame, reference frame, space): Specified by the position of origin, axis directions, and distance unit. All coordinate systems in 3D Slicer are right-handed.

Extension (or Slicer extension): A collection of modules that is not bundled with the core application but can be downloaded and installed using the Extensions manager.

Extensions manager: A software component of Slicer that allows browsing, installing, uninstalling extensions in the Extensions catalog (also known as the Slicer app store) directly from the application.

Extensions index: A repository that contains description of each extension that the Extension catalog is built from.

Extent: Range of integer coordinates along 3 axes. Defined in VTK by 6 values, for IJK axes: I_min, I_max, J_min, J_max, K_min, K_max. Both minimum and maximum values are inclusive, therefore size of an array is (I_max - I_min + 1) x (J_max - J_min + 1) x (K_max - K_min + 1).

Fiducial: Represents a point in 3D space. The term originates from image-guided surgery, where “fiducial markers” are used to mark point positions.

Frame: One time point in a time sequence. To avoid ambiguity, this term is not used to refer to a slice of a volume.

Geometry: Specifies location and shape of an object in 3D space. See “Volume” term for definition of image geometry.

Image intensity: Typically refers to the value of a voxel. Displayed pixel brightness and color is computed from this value based on the chosen window/level and color lookup table.

IJK: Voxel coordinate system axes. Integer coordinate values correspond to voxel center positions. IJK values are often used as coordinate values to designate an element within a 3D array. By VTK convention, and I indexes the column, J indexes the row, K indexes the slice. Note that numpy uses the opposite ordering convention, where a[K][J][I]. Sometimes this memory layout is described as I being the fastest moving index and K being the slowest moving.

ITK: Insight Toolkit. Software library that Slicer uses for most image processing operations.

Labelmap (or labelmap volume, labelmap volume node): Volume node that has discrete (integer) voxel values. Typically each value corresponds to a specific structure or region. This allows compact representation of non-overlapping regions in a single 3D array. Most software use a single labelmap to store an image segmentation, but Slicer uses a dedicated segmentation node, which can contain multiple representations (multiple labelmaps to allow storing overlapping segments; closed surface representation for quick 3D visualization, etc.).

LPS: Left-posterior-superior anatomical coordinate system. Most commonly used coordinate system in medical image computing. Slicer stores all data in LPS coordinate system on disk (and converts to/from RAS when writing to or reading from disk).

Markups: Simple geometric objects and measurements that the user can place in viewers. Markups module can be used to create such objects. There are several types, such as point list, line, curve, plane, ROI.

Source volume: Voxel values of this volume is used during segmentation by those effects that rely on the intensity of an underlying volume.

MRML: Medical Reality Markup Language: Software library for storage, visualization, and processing of information objects that may be used in medical applications. The library is designed to be reusable in various software applications, but 3D Slicer is the only major application that is known to use it.

Model (or model node): MRML node storing surface mesh (consists of triangle, polygon, or other 2D cells) or volumetric mesh (consists of tetrahedral, wedge, or other 3D cells)

Module (or Slicer module): A Slicer module is a software component consisting of a graphical user interface (that is displayed in the module panel when the module is selected), a logic (that implements algorithms that operate on MRML nodes), and may provide new MRML node types, displayable managers (that are responsible for displaying those nodes in views), input/output plugins (that are responsible for load/save MRML nodes in files), and various other plugins. Modules are typically independent and only communicate with each other via modifying MRML nodes, but sometimes a module use features provided by other modules by calling methods in its logic.

Node (or MRML node): One data object in the scene. A node can represent data (such as an image or a mesh), describe how it is displayed (color, opacity, etc.), stored on disk, spatial transformations applied on them, etc. There is a C++ class hierarchy to define the common behaviors of nodes, such as the property of being storable on disk or being geometrically transformable. The structure of this class hierarchy can be inspected in the code or in the API documentation.

Orientation marker: Arrow, box, or human shaped marker to show axis directions in slice views and 3D views.

RAS: Right-anterior-superior anatomical coordinate system. Coordinate system used internally in Slicer. It can be converted to/from LPS coordinate system by inverting the direction of the first two axes.

Reference: Has no specific meaning, but typically refers to a secondary input (data object, coordinate frame, geometry, etc.) for an operation.

Region of interest (ROI): Specifies a box-shaped region in 3D. Can be used for cropping volumes, clipping models, etc.

Registration: The process of aligning objects in space. Result of the registration is a transform, which transforms the “moving” object to the “fixed” object.

Resolution: Voxel size of a volume, typically specified in mm/pixel. It is rarely used in the user interface because its meaning is slightly misleading: high resolution value means large spacing, which means coarse (low) image resolution.

Ruler: It may refer to: 1. View ruler: The line that is displayed as an overlay in viewers to serve as a size reference. 2. Markups line: distance measurement tool.

Scalar component: One element of a vector. Number of scalar components means the length of the vector.

Scalar value: A simple number. Typically floating-point.

Scene (or MRML scene): This is the data structure that contains all the data that is currently loaded into the application and additional information about how they should be displayed or used. The term originates from computer graphics.

Segment: Corresponds to a single structure in a segmentation. See more information in the Image segmentation section.

Segmentation (also known as contouring, annotation; region of interest, structure set, mask): Process of delineating 3D structures in images. Segmentation can also refer to the MRML node that is the result of the segmentation process. A segmentation node typically contains multiple segments (each segment corresponds to one 3D structure). Segmentation nodes are not labelmap nodes or model nodes but they can store multiple representations (binary labelmap, closed surface, etc.). See more information in Image segmentation section.

Slice: Intersection of a 3D object with a plane.

Slice view annotations: text in corner of slice views displaying name, and selected DICOM tags of the displayed volumes

Spacing: Voxel size of a volume, typically specified in mm/pixel.

Transform (or transformation): Can transform any 3D object from one coordinate system to another. Most common type is rigid transform, which can change position and orientation of an object. Linear transforms can scale, mirror, shear objects. Non-linear transforms can arbitrarily warp the 3D space. To display a volume in the world coordinate system, the volume has to be resampled, therefore transform from the world coordinate system to the volume is needed (it is called the resampling transform). To transform all other node types to the world coordinate system, all points must be transformed to the world coordinate system (modeling transform). Since a transform node must be applicable to any nodes, transform nodes can provide both from and to the parent (store one and compute the other on-the-fly).

Volume (or volume node, scalar volume, image): MRML node storing 3D array of voxels. Indices of the array are typically referred to as IJK. Range of IJK coordinates are called extents. Geometry of the volume is specified by its origin (position of the IJK=(0,0,0) point), spacing (size of a voxel along I, J, K axes), axis directions (direction of I, J, K axes in the reference coordinate system) with respect to a frame of reference. 2D images are single-slice 3D volumes, with their position and orientation specified in 3D space.

Voxel: One element of a 3D volume. It has a rectangular prism shape. Coordinates of a voxel correspond to the position of its center point. Value of a voxel may be a simple scalar value or a vector.

VR: Abbreviation that can refer to volume rendering or virtual reality. To avoid ambiguity it is generally recommended to use the full term instead (or explicitly define the meaning of the abbreviation in the given context).

VTK: Visualization Toolkit. Software library that Slicer uses for to data representation and visualization. Since most Slicer classes are derived from VTK classes and they heavily use other VTK classes, Slicer adopted many conventions of VTK style and application programming interface.

Window/level (or window width/window level): Specifies linear mapping of voxel values to the brightness of a displayed pixel. Window is the size of the intensity range that is mapped to the full displayable intensity range. Level is the voxel value that is mapped to the center of the full displayable intensity range.

