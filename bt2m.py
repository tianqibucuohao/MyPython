#使用Python实现BT种子和磁力链接的相互转换

#相应的将BT种子转换为磁力链代码为：
import bencode, hashlib, base64, urllib
torrent = open('ubuntu-12.04.2-server-amd64.iso.torrent', 'rb').read()
metadata = bencode.bdecode(torrent)
hashcontents = bencode.bencode(metadata['info'])
digest = hashlib.sha1(hashcontents).digest()
b32hash = base64.b32encode(digest)
params = {'xt': 'urn:btih:%s' % b32hash,
      'dn': metadata['info']['name'],
      'tr': metadata['announce'],
      'xl': metadata['info']['length']}
paramstr = urllib.urlencode(params)
magneturi = 'magnet:?%s' % paramstr
print(magneturi)

#还有另外一个效率相对较高，而且更方便的方案是安装libtorrent
# 在ubuntu只需要apt-get install python-libtorrent即可对应转换磁力链的代码为：
import libtorrent as bt
info = bt.torrent_info('test.torrent')
print ("magnet:?xt=urn:btih:%s&dn=%s" % (info.info_hash(), info.name()))
#转换磁力链接为bt种子文件

#下面来看一个反过程，将磁力链转化为种子文件。
#需要先安装python-libtorrent包 ，在ubuntu环境下，可以通过以下指令完成安装：
import shutil
import tempfile
import os.path as pt
import sys
import libtorrent as lt
from time import sleep
def magnet2torrent(magnet, output_name=None):
  if output_name and \
      not pt.isdir(output_name) and \
      not pt.isdir(pt.dirname(pt.abspath(output_name))):
    print("Invalid output folder: " + pt.dirname(pt.abspath(output_name)))
    print("")
    sys.exit(0)
  tempdir = tempfile.mkdtemp()
  ses = lt.session()
  params = {
    'save_path': tempdir,
    'duplicate_is_error': True,
    'storage_mode': lt.storage_mode_t(2),
    'paused': False,
    'auto_managed': True,
    'duplicate_is_error': True
  }
  handle = lt.add_magnet_uri(ses, magnet, params)
  print("Downloading Metadata (this may take a while)")
  while (not handle.has_metadata()):
    try:
      sleep(1)
    except KeyboardInterrupt:
      print("Aborting...")
      ses.pause()
      print("Cleanup dir " + tempdir)
      shutil.rmtree(tempdir)
      sys.exit(0)
  ses.pause()
  print("Done")
  torinfo = handle.get_torrent_info()
  torfile = lt.create_torrent(torinfo)
  output = pt.abspath(torinfo.name() + ".torrent")
  if output_name:
    if pt.isdir(output_name):
      output = pt.abspath(pt.join(
        output_name, torinfo.name() + ".torrent"))
    elif pt.isdir(pt.dirname(pt.abspath(output_name))):
      output = pt.abspath(output_name)
  print("Saving torrent file here : " + output + " ...")
  torcontent = lt.bencode(torfile.generate())
  f = open(output, "wb")
  f.write(lt.bencode(torfile.generate()))
  f.close()
  print("Saved! Cleaning up dir: " + tempdir)
  ses.remove_torrent(handle)
  shutil.rmtree(tempdir)
  return output
def showHelp():
  print("")
  print("USAGE: " + pt.basename(sys.argv[0]) + " MAGNET [OUTPUT]")
  print(" MAGNET\t- the magnet url")
  print(" OUTPUT\t- the output torrent file name")
  print("")
def main():
  if len(sys.argv) < 2:
    showHelp()
    sys.exit(0)
  magnet = sys.argv[1]
  output_name = None
  if len(sys.argv) >= 3:
    output_name = sys.argv[2]
  magnet2torrent(magnet, output_name)
if __name__ == "__main__":
  main()