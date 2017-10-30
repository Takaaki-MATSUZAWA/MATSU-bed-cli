# MATSU-bed-cli

## インストール方法
### 前準備
- Python のインストール: https://www.python.org/downloads/
- Git のインストール: https://git-scm.com/download
- Mercurial のインストール: https://www.mercurial-scm.org/
- GCC のインストール: https://launchpad.net/gcc-arm-embedded/4.9/4.9-2015-q3-update
- mbed-cliのinstall:`pip install mbed-cli`

pipが入っていればMATSU-bed-cliを入れる時にmbed-cliも一緒に入るはず
## 本体のインストール
コマンドプロンプトで
```
> git clone https://github.com/hardtail0112/MATSU-bed-cli

> cd MATSU-bed-cli
> python setup.py install
```

## 動作確認
コマンドプロンプトで
```
> matsubed --version
0.1.0
```

## 環境構築
適当な場所にworkspaceを作る
```
> mkdir matsubed-workspace
> cd matsubed-workspace
> matsubed init
```
mbedのライブラリをまるごと落としてくるので結構時間がかかる

## 使い方
### 新しいプロジェクトの作成
例えばLED_blinkというプロジェクトを作る。

workspaceで
```
> matsubed new LED_blink
> cd LED_blink
> matsubed compile
```

### mbed.orgからインポート
例えばMATSU-bed_blinkyをインポートする

workspaceで
```
> matsubed import https://developer.mbed.org/users/hardtail/code/MATSU-bed_blinky/
> cd MATSU-bed_blinky
> matsubed compile
```

### ライブラリの追加
例えばMPU6050のDMP用のライブラリを落としてくる

#### オンラインから追加
ライブラリをインポートしたいプロジェクトの中で
```
> matsubed add https://os.mbed.com/users/hardtail/code/MPU6050_DMP_test_for1549/

```

#### 既にダウンロードしたライブラリを確認
一度ダウンロードしたライブラリはlibraryフォルダに入ってる
以下のコマンドで確認できる
```
> matsubed library

List of libraries being downloaded
   mbed
   MPU6050-DMP
   pwm_all_out
   USBDevice
```

#### 既にlibraryフォルダにあるライブラリを追加
ライブラリをインポートしたいプロジェクトの中で
```
> matsubed add MPU6050-DMP
```

### コンパイル
コンパイルしたいプロジェクトの中で
```
> matsubed compile

..
+----------------------------------------------------------------------+-------+-------+------+
| Module                                                               | .text | .data | .bss |
+----------------------------------------------------------------------+-------+-------+------+
| BUILD\LPC1549\GCC_ARM\USBDevice\USBAudio\USBAudio.o                  |    30 |     0 |    0 |
| BUILD\LPC1549\GCC_ARM\USBDevice\USBDevice\USBDevice.o                |  1728 |    98 |    6 |
| BUILD\LPC1549\GCC_ARM\USBDevice\USBDevice\USBHAL_LPC11U.o            |  2198 |     4 | 2232 |
| BUILD\LPC1549\GCC_ARM\USBDevice\USBHID\USBKeyboard.o                 |    34 |     0 |    0 |
| BUILD\LPC1549\GCC_ARM\USBDevice\USBSerial\USBCDC.o                   |   544 |   130 |    4 |
| BUILD\LPC1549\GCC_ARM\USBDevice\USBSerial\USBSerial.o                |   578 |     0 |    0 |
| BUILD\LPC1549\GCC_ARM\main.o                                         |   607 |     4 |  452 |
| [fill]                                                               |    59 |     4 | 1395 |
| [lib]/c_nano.a                                                       |  6074 |   100 |   12 |
| [lib]/gcc.a                                                          |   748 |     0 |    0 |
| [lib]/mbed.a                                                         |  3424 |     0 |   42 |
| [lib]/misc                                                           |   252 |    12 |   28 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\gpio_api.o        |   327 |     0 |    4 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\gpio_irq_api.o    |   492 |     0 |   36 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\mbed_board.o      |   378 |     0 |    0 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\mbed_retarget.o   |  1569 |     4 |  272 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\mbed_sdk_boot.o   |    80 |     0 |    0 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\pinmap.o          |   187 |     0 |    0 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\serial_api.o      |   952 |     0 |   17 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\startup_LPC15xx.o |   320 |     0 |    0 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\system_LPC15xx.o  |   204 |     4 |    0 |
| mbed\fb8e0ae1cceb\TARGET_LPC1549\TOOLCHAIN_GCC_ARM\us_ticker.o       |   276 |     0 |    4 |
| Subtotals                                                            | 21061 |   360 | 4504 |
+----------------------------------------------------------------------+-------+-------+------+
Total Static RAM memory (data + bss): 4864 bytes
Total Flash memory (text + data): 21421 bytes

Image: .\BUILD\LPC1549\GCC_ARM\library.bin
```
最後にこんな感じのが出ればコンパイル成功

### MATSU-bedへの書き込み
MATSU-bedをUSB-ISPモードでPCに接続してから
書き込みたいプロジェクトの中で
```
> matsubed flash

Success firmware update !!!
```
