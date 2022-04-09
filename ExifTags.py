#
# The Python Imaging Library.
# $Id$
#
# EXIF tags
#
# Copyright (c) 2003 by Secret Labs AB
#
# See the README file for information on usage and redistribution.
#

"""
This module provides constants and clear-text names for various
well-known EXIF tags.
"""


TAGS = {
    # possibly incomplete
    0x0001: "InteropIndex",
    0x000B: "ProcessingSoftware",
    0x00FE: "NewSubfileType",
    0x00FF: "SubfileType",
    0x0100: "ImageWidth",
    0x0101: "ImageLength",
    0x0102: "BitsPerSample",
    0x0103: "Compression",
    0x0106: "PhotometricInterpretation",
    0x0107: "Thresholding",
    0x0108: "CellWidth",
    0x0109: "CellLength",
    0x010A: "FillOrder",
    0x010D: "DocumentName",
    0x010E: "ImageDescription",
    0x010F: "Make",
    0x0110: "Model",
    0x0111: "StripOffsets",
    0x0112: "Orientation",
    0x0115: "SamplesPerPixel",
    0x0116: "RowsPerStrip",
    0x0117: "StripByteCounts",
    0x0118: "MinSampleValue",
    0x0119: "MaxSampleValue",
    0x011A: "XResolution",
    0x011B: "YResolution",
    0x011C: "PlanarConfiguration",
    0x011D: "PageName",
    0x0120: "FreeOffsets",
    0x0121: "FreeByteCounts",
    0x0122: "GrayResponseUnit",
    0x0123: "GrayResponseCurve",
    0x0124: "T4Options",
    0x0125: "T6Options",
    0x0128: "ResolutionUnit",
    0x0129: "PageNumber",
    0x012D: "TransferFunction",
    0x0131: "Software",
    0x0132: "DateTime",
    0x013B: "Artist",
    0x013C: "HostComputer",
    0x013D: "Predictor",
    0x013E: "WhitePoint",
    0x013F: "PrimaryChromaticities",
    0x0140: "ColorMap",
    0x0141: "HalftoneHints",
    0x0142: "TileWidth",
    0x0143: "TileLength",
    0x0144: "TileOffsets",
    0x0145: "TileByteCounts",
    0x014A: "SubIFDs",
    0x014C: "InkSet",
    0x014D: "InkNames",
    0x014E: "NumberOfInks",
    0x0150: "DotRange",
    0x0151: "TargetPrinter",
    0x0152: "ExtraSamples",
    0x0153: "SampleFormat",
    0x0154: "SMinSampleValue",
    0x0155: "SMaxSampleValue",
    0x0156: "TransferRange",
    0x0157: "ClipPath",
    0x0158: "XClipPathUnits",
    0x0159: "YClipPathUnits",
    0x015A: "Indexed",
    0x015B: "JPEGTables",
    0x015F: "OPIProxy",
    0x0200: "JPEGProc",
    0x0201: "JpegIFOffset",
    0x0202: "JpegIFByteCount",
    0x0203: "JpegRestartInterval",
    0x0205: "JpegLosslessPredictors",
    0x0206: "JpegPointTransforms",
    0x0207: "JpegQTables",
    0x0208: "JpegDCTables",
    0x0209: "JpegACTables",
    0x0211: "YCbCrCoefficients",
    0x0212: "YCbCrSubSampling",
    0x0213: "YCbCrPositioning",
    0x0214: "ReferenceBlackWhite",
    0x02BC: "XMLPacket",
    0x1000: "RelatedImageFileFormat",
    0x1001: "RelatedImageWidth",
    0x1002: "RelatedImageLength",
    0x4746: "Rating",
    0x4749: "RatingPercent",
    0x800D: "ImageID",
    0x828D: "CFARepeatPatternDim",
    0x828E: "CFAPattern",
    0x828F: "BatteryLevel",
    0x8298: "Copyright",
    0x829A: "ExposureTime",
    0x829D: "FNumber",
    0x83BB: "IPTCNAA",
    0x8649: "ImageResources",
    0x8769: "ExifOffset",
    0x8773: "InterColorProfile",
    0x8822: "ExposureProgram",
    0x8824: "SpectralSensitivity",
    0x8825: "GPSInfo",
    0x8827: "ISOSpeedRatings",
    0x8828: "OECF",
    0x8829: "Interlace",
    0x882A: "TimeZoneOffset",
    0x882B: "SelfTimerMode",
    0x8830: "SensitivityType",
    0x8831: "StandardOutputSensitivity",
    0x8832: "RecommendedExposureIndex",
    0x8833: "ISOSpeed",
    0x8834: "ISOSpeedLatitudeyyy",
    0x8835: "ISOSpeedLatitudezzz",
    0x9000: "ExifVersion",
    0x9003: "DateTimeOriginal",
    0x9004: "DateTimeDigitized",
    0x9010: "OffsetTime",
    0x9011: "OffsetTimeOriginal",
    0x9012: "OffsetTimeDigitized",
    0x9101: "ComponentsConfiguration",
    0x9102: "CompressedBitsPerPixel",
    0x9201: "ShutterSpeedValue",
    0x9202: "ApertureValue",
    0x9203: "BrightnessValue",
    0x9204: "ExposureBiasValue",
    0x9205: "MaxApertureValue",
    0x9206: "SubjectDistance",
    0x9207: "MeteringMode",
    0x9208: "LightSource",
    0x9209: "Flash",
    0x920A: "FocalLength",
    0x920B: "FlashEnergy",
    0x920C: "SpatialFrequencyResponse",
    0x920D: "Noise",
    0x9211: "ImageNumber",
    0x9212: "SecurityClassification",
    0x9213: "ImageHistory",
    0x9214: "SubjectLocation",
    0x9215: "ExposureIndex",
    0x9216: "TIFF/EPStandardID",
    0x927C: "MakerNote",
    0x9286: "UserComment",
    0x9290: "SubsecTime",
    0x9291: "SubsecTimeOriginal",
    0x9292: "SubsecTimeDigitized",
    0x9400: "AmbientTemperature",
    0x9401: "Humidity",
    0x9402: "Pressure",
    0x9403: "WaterDepth",
    0x9404: "Acceleration",
    0x9405: "CameraElevationAngle",
    0x9C9B: "XPTitle",
    0x9C9C: "XPComment",
    0x9C9D: "XPAuthor",
    0x9C9E: "XPKeywords",
    0x9C9F: "XPSubject",
    0xA000: "FlashPixVersion",
    0xA001: "ColorSpace",
    0xA002: "ExifImageWidth",
    0xA003: "ExifImageHeight",
    0xA004: "RelatedSoundFile",
    0xA005: "ExifInteroperabilityOffset",
    0xA20B: "FlashEnergy",
    0xA20C: "SpatialFrequencyResponse",
    0xA20E: "FocalPlaneXResolution",
    0xA20F: "FocalPlaneYResolution",
    0xA210: "FocalPlaneResolutionUnit",
    0xA214: "SubjectLocation",
    0xA215: "ExposureIndex",
    0xA217: "SensingMethod",
    0xA300: "FileSource",
    0xA301: "SceneType",
    0xA302: "CFAPattern",
    0xA401: "CustomRendered",
    0xA402: "ExposureMode",
    0xA403: "WhiteBalance",
    0xA404: "DigitalZoomRatio",
    0xA405: "FocalLengthIn35mmFilm",
    0xA406: "SceneCaptureType",
    0xA407: "GainControl",
    0xA408: "Contrast",
    0xA409: "Saturation",
    0xA40A: "Sharpness",
    0xA40B: "DeviceSettingDescription",
    0xA40C: "SubjectDistanceRange",
    0xA420: "ImageUniqueID",
    0xA430: "CameraOwnerName",
    0xA431: "BodySerialNumber",
    0xA432: "LensSpecification",
    0xA433: "LensMake",
    0xA434: "LensModel",
    0xA435: "LensSerialNumber",
    0xA460: "CompositeImage",
    0xA461: "CompositeImageCount",
    0xA462: "CompositeImageExposureTimes",
    0xA500: "Gamma",
    0xC4A5: "PrintImageMatching",
    0xC612: "DNGVersion",
    0xC613: "DNGBackwardVersion",
    0xC614: "UniqueCameraModel",
    0xC615: "LocalizedCameraModel",
    0xC616: "CFAPlaneColor",
    0xC617: "CFALayout",
    0xC618: "LinearizationTable",
    0xC619: "BlackLevelRepeatDim",
    0xC61A: "BlackLevel",
    0xC61B: "BlackLevelDeltaH",
    0xC61C: "BlackLevelDeltaV",
    0xC61D: "WhiteLevel",
    0xC61E: "DefaultScale",
    0xC61F: "DefaultCropOrigin",
    0xC620: "DefaultCropSize",
    0xC621: "ColorMatrix1",
    0xC622: "ColorMatrix2",
    0xC623: "CameraCalibration1",
    0xC624: "CameraCalibration2",
    0xC625: "ReductionMatrix1",
    0xC626: "ReductionMatrix2",
    0xC627: "AnalogBalance",
    0xC628: "AsShotNeutral",
    0xC629: "AsShotWhiteXY",
    0xC62A: "BaselineExposure",
    0xC62B: "BaselineNoise",
    0xC62C: "BaselineSharpness",
    0xC62D: "BayerGreenSplit",
    0xC62E: "LinearResponseLimit",
    0xC62F: "CameraSerialNumber",
    0xC630: "LensInfo",
    0xC631: "ChromaBlurRadius",
    0xC632: "AntiAliasStrength",
    0xC633: "ShadowScale",
    0xC634: "DNGPrivateData",
    0xC635: "MakerNoteSafety",
    0xC65A: "CalibrationIlluminant1",
    0xC65B: "CalibrationIlluminant2",
    0xC65C: "BestQualityScale",
    0xC65D: "RawDataUniqueID",
    0xC68B: "OriginalRawFileName",
    0xC68C: "OriginalRawFileData",
    0xC68D: "ActiveArea",
    0xC68E: "MaskedAreas",
    0xC68F: "AsShotICCProfile",
    0xC690: "AsShotPreProfileMatrix",
    0xC691: "CurrentICCProfile",
    0xC692: "CurrentPreProfileMatrix",
    0xC6BF: "ColorimetricReference",
    0xC6F3: "CameraCalibrationSignature",
    0xC6F4: "ProfileCalibrationSignature",
    0xC6F6: "AsShotProfileName",
    0xC6F7: "NoiseReductionApplied",
    0xC6F8: "ProfileName",
    0xC6F9: "ProfileHueSatMapDims",
    0xC6FA: "ProfileHueSatMapData1",
    0xC6FB: "ProfileHueSatMapData2",
    0xC6FC: "ProfileToneCurve",
    0xC6FD: "ProfileEmbedPolicy",
    0xC6FE: "ProfileCopyright",
    0xC714: "ForwardMatrix1",
    0xC715: "ForwardMatrix2",
    0xC716: "PreviewApplicationName",
    0xC717: "PreviewApplicationVersion",
    0xC718: "PreviewSettingsName",
    0xC719: "PreviewSettingsDigest",
    0xC71A: "PreviewColorSpace",
    0xC71B: "PreviewDateTime",
    0xC71C: "RawImageDigest",
    0xC71D: "OriginalRawFileDigest",
    0xC71E: "SubTileBlockSize",
    0xC71F: "RowInterleaveFactor",
    0xC725: "ProfileLookTableDims",
    0xC726: "ProfileLookTableData",
    0xC740: "OpcodeList1",
    0xC741: "OpcodeList2",
    0xC74E: "OpcodeList3",
    0xC761: "NoiseProfile",
}
"""Maps EXIF tags to tag names."""


GPSTAGS = {
    0: "GPSVersionID",
    1: "GPSLatitudeRef",
    2: "GPSLatitude",
    3: "GPSLongitudeRef",
    4: "GPSLongitude",
    5: "GPSAltitudeRef",
    6: "GPSAltitude",
    7: "GPSTimeStamp",
    8: "GPSSatellites",
    9: "GPSStatus",
    10: "GPSMeasureMode",
    11: "GPSDOP",
    12: "GPSSpeedRef",
    13: "GPSSpeed",
    14: "GPSTrackRef",
    15: "GPSTrack",
    16: "GPSImgDirectionRef",
    17: "GPSImgDirection",
    18: "GPSMapDatum",
    19: "GPSDestLatitudeRef",
    20: "GPSDestLatitude",
    21: "GPSDestLongitudeRef",
    22: "GPSDestLongitude",
    23: "GPSDestBearingRef",
    24: "GPSDestBearing",
    25: "GPSDestDistanceRef",
    26: "GPSDestDistance",
    27: "GPSProcessingMethod",
    28: "GPSAreaInformation",
    29: "GPSDateStamp",
    30: "GPSDifferential",
    31: "GPSHPositioningError",
}
"""Maps EXIF GPS tags to tag names."""