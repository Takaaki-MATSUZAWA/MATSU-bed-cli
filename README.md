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
> git clone https://github.com/Takaaki-MATSUZAWA/MATSU-bed-cli

> cd MATSU-bed-cli
> python setup.py install
```

## 動作確認
```
> matsubed --version
0.1.0
```

## 環境構築
適当な場所にworkspaceを作ってその中でinitコマンドを実行
```
> mkdir matsubed-workspace
> cd matsubed-workspace

matsubed-workspace> matsubed init
```
mbedのライブラリをまるごと落としてくるので結構時間がかかる

## 使い方
1. プロジェクト作成or追加
2. ライブラリの追加
3. コンパイル
4. MATSU-bedへの書き込み
### **1. プロジェクトの作成or追加**
プロジェクトはnewコマンドを使って作成する方法と、mbed.orgからインポートする方法がある。
#### 新しいプロジェクトの作成
workspaceでnewコマンドを実行

例えばLED_blinkというプロジェクトを作る場合
```
matsubed-workspace> matsubed new LED_blink
```

#### mbed.orgからインポート
例えばMATSU-bed_blinkyをインポートする
```
matsubed-workspace> matsubed import https://developer.mbed.org/users/hardtail/code/MATSU-bed_blinky/
```

### **2. ライブラリの追加**
コンパイルに必要なライブラリを追加する。

オンラインから追加する方法と、すでにダウンロードしたライブラリから追加する方法がある。

#### オンラインから追加
例えばLED_blinkにMPU6050のDMP用のライブラリを追加する

ライブラリをインポートしたいプロジェクトの中でaddコマンドを実行
```
matsubed-workspace\LED_blink> matsubed add https://os.mbed.com/users/hardtail/code/MPU6050_DMP_test_for1549/

```

#### 既にlibraryフォルダにあるライブラリを追加
一度ダウンロードしたライブラリはlibraryフォルダに入ってる

libraryのコマンドで確認
```
> matsubed library

List of libraries being downloaded
   mbed
   MPU6050-DMP
   USBD
```
この場合は、ライブラリ名だけで追加できる

addコマンドで追加
```
matsubed-workspace\LED_blink> matsubed add MPU6050-DMP
```

上記のコマンドがうまくいかない場合:
 - 管理者権限でコマンドプロンプトを開き、addコマンドを実行しなおす

 または
 - libraryフォルダから必要なライブラリを、プロジェクトフォルダ内にコピーして「3.コンパイル」に進む。

### **3. コンパイル**
コンパイルしたいプロジェクトのフォルダのなかでcompileコマンドを実行
```
matsubed-workspace\LED_blink> matsubed compile

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

Image: .\BUILD\LPC1549\GCC_ARM\LED_blink.bin
```
最後にこんな感じのが出ればコンパイル成功

### **4. MATSU-bedへの書き込み**
MATSU-bedをUSB-ISPモードでPCに接続する

書き込みたいプロジェクトの中でflashコマンドを実行
```
matsubed-workspace\LED_blink> matsubed flash

Success firmware update !!!
```
