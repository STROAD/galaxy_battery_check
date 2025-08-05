# galaxy battery check
Simple Python Script to Check Battery Life on Samsung Galaxy Phones Using ADB  
ADB를 이용해 갤럭시 스마트폰에서 배터리 수명을 확인하는 간단한 파이썬 스크립트

## Requirements
This script requires **Python 3.x**  
이 스크립트는 **Python 3.x**가 필요합니다.

You need to install pure-python-adb:  
pure-python-adb를 설치해야 합니다:
```
pip install pure-python-adb
```

## Quick Start Guide
1. **Download ADB**: ADB must be installed. You can download it from [here](https://developer.android.com/tools/adb).  
**ADB 다운로드**: ADB가 설치되어 있어야 합니다. ADB는 [여기](https://developer.android.com/tools/adb)에서 다운로드할 수 있습니다.
2. **Enable USB Debugging**: USB debugging must be enabled on your smartphone. Go to Settings > Developer Options > Enable USB Debugging.  
**USB 디버깅 활성화**: 스마트폰에서 USB 디버깅을 활성화해야 합니다. 설정 > 개발자 옵션 > USB 디버깅을 활성화하세요.
3. **Clone Repository**: Clone this repository or [download it as a zip file]((https://github.com/STROAD/galaxy_battery_check/archive/refs/heads/main.zip)).  
**리포지토리 클론**: 이 저장소를 클론하거나 [zip 파일로 다운로드](https://github.com/STROAD/galaxy_battery_check/archive/refs/heads/main.zip)합니다.
   ```bash
   git clone https://github.com/STROAD/galaxy_battery_check.git
   ```
4. **Set ADB Path**: After extracting the downloaded ADB package, copy the `platform-tools` folder into the `galaxy_battery_check` folder.  
**ADB 경로 설정**: 다운로드 받은 adb파일을 압축해제 후 `platform-tools` 폴더를 `galaxy_battery_check` 폴더에 복사합니다.
5. **Run Script**: Execute the script using Python.  
**스크립트 실행**: 스크립트를 실행합니다.
   ```bash
   python main.py
   ```
