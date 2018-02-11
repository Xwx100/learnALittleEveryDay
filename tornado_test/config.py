import os

BaseDir = os.path.dirname(__file__)
settings = {
    'static_path':os.path.join(BaseDir, 'static'),
    'template_path':os.path.join(BaseDir, 'template'),
    'debug':True,
    'cookie_secret':'HMNmfR5GR1CcxIRiUaA5T1MvcTC8EU1FrdIuGrSfb2U='
}