Title: 黑苹果创建FunsionDrive
Date: 2022-2-26 16:54
Category: 折腾

```
yuanch@192 ~ % diskutil list
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *250.1 GB   disk0
   1:                        EFI EFI                     209.7 MB   disk0s1
   2:                 Apple_APFS Container disk2         249.8 GB   disk0s2

/dev/disk1 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *512.1 GB   disk1
   1:                        EFI EFI                     209.7 MB   disk1s1
   2:                 Apple_APFS Container disk3         511.9 GB   disk1s2

/dev/disk2 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +249.8 GB   disk2
                                 Physical Store disk0s2
   1:                APFS Volume Preboot                 28.7 KB    disk2s2
   2:                APFS Volume Recovery                20.5 KB    disk2s3
   3:                APFS Volume VM                      1.1 MB     disk2s4

/dev/disk3 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +511.9 GB   disk3
                                 Physical Store disk1s2
   1:                APFS Volume macOS - 数据            6.0 GB     disk3s1
   2:                APFS Volume Preboot                 284.2 MB   disk3s2
   3:                APFS Volume Recovery                622.1 MB   disk3s3
   4:                APFS Volume VM                      1.1 MB     disk3s4
   5:                APFS Volume macOS                   15.3 GB    disk3s5
   6:              APFS Snapshot com.apple.os.update-... 15.3 GB    disk3s5s1

/dev/disk4 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *31.0 GB    disk4
   1:                        EFI EFI                     209.7 MB   disk4s1
   2:                  Apple_HFS Install macOS Big Sur   13.2 GB    disk4s2
                    (free space)                         134.8 MB   -
   3:       Microsoft Basic Data OC                      398.5 MB   disk4s3
   4:       Microsoft Basic Data CLOVER                  399.5 MB   disk4s4
   5:       Microsoft Basic Data WEPE                    558.9 MB   disk4s5
                    (free space)                         16.1 GB    -

/dev/disk5 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *8.0 TB     disk5
   1:                        EFI EFI                     209.7 MB   disk5s1
   2:                 Apple_APFS Container disk6         8.0 TB     disk5s2

/dev/disk6 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +8.0 TB     disk6
                                 Physical Store disk5s2
```
```
yuanch@192 ~ % diskutil apfs
Usage:  diskutil [quiet] ap[fs] <verb> <options>
        where <verb> is as follows:

     list                (Show status of all current APFS Containers)
     listUsers           (List cryptographic users/keys of an APFS Volume)
     listSnapshots       (List APFS Snapshots in a mounted APFS Volume)
     listVolumeGroups    (List all current APFS Volume Group relationships)
     convert             (Nondestructively convert from HFS to APFS)
     create              (Create a new APFS Container with one APFS Volume)
     createContainer     (Create a new empty APFS Container)
     deleteContainer     (Delete an APFS Container and free or reformat disks)
     resizeContainer     (Resize an APFS Container and its disk space usage)
     addVolume           (Export a new APFS Volume from an APFS Container)
     deleteVolume        (Remove an APFS Volume from its APFS Container)
     deleteVolumeGroup   (Remove grouped APFS Volumes from its APFS Container)
     eraseVolume         (Erase contents of, but keep, an APFS Volume)
     changeVolumeRole    (Change the Role metadata flags of an APFS Volume)
     unlockVolume        (Unlock an encrypted APFS Volume which is locked)
     lockVolume          (Lock an encrypted APFS Volume (diskutil unmount))
     changePassphrase    (Change the passphrase of a cryptographic user)
     setPassphraseHint   (Set or clear passphrase hint of a cryptographic user)
     encryptVolume       (Enable FileVault security in background or instantly)
     decryptVolume       (Disable FileVault security in background or instantly)
     deleteSnapshot      (Remove an APFS Snapshot from an APFS Volume)
     defragment          (Arm or check status or begin APFS defragmentation)
     updatePreboot       (Update a macOS Volume's related APFS Preboot Volume)
     syncPatchUsers      (Copy Volume Group crypto users System-to-Data role)

diskutil apfs <verb> with no options will provide help on that verb

yuanch@192 ~ % diskutil apfs createContainer 
Usage:  diskutil apfs createContainer <disk> [<disk>]
        diskutil apfs createContainer -main <disk> [-secondary <disk>]
        where <disk> = MountPoint|DiskIdentifier|DeviceNode
Create an empty APFS Container. You can then add APFS Volumes with the
diskutil apfs addVolume verb. If you specify two disks, then a "Fusion"
Container is created. If you specify these two disks without the keywords
"-main" and "-secondary", then their performance duties are assigned
automatically, with the requirement that their rotational/solid-state design
be identifiable (often not the case for external disks). If you do specify
explicit "-main" and "-secondary" options, the "main" disk is assumed to
be "faster" (you should use solid-state hardware if available), while the
"secondary" disk is assumed to be "slower". The "secondary" disk is
often used to store associated "auxiliary" data, such as a Boot Camp
Assistant partition. Ownership of any affected disks is required.
Example:  diskutil apfs createContainer disk0s2
yuanch@192 ~ % diskutil apfs createContainer -main disk0 -secondary disk5
Creating container with disk0 disk5
Started APFS operation on disk0
Creating a new empty APFS Container
Unmounting Volumes
Switching disk0 to APFS
Switching disk5 to APFS
Creating APFS Container
FusionLC autodetect: regular Fusion
Created new APFS Container disk2
Disk from APFS operation: disk2
Finished APFS operation on disk0
```

```
yuanch@CharlesdeiMac ~ % diskutil list
/dev/disk0 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                                                   *250.1 GB   disk0

/dev/disk1 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *512.1 GB   disk1
   1:                        EFI EFI                     209.7 MB   disk1s1
   2:                 Apple_APFS Container disk3         511.9 GB   disk1s2

/dev/disk2 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *128.0 GB   disk2
   1:                        EFI NO NAME                 272.6 MB   disk2s1
   2:                 Apple_APFS Container disk4         127.7 GB   disk2s2

/dev/disk3 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +511.9 GB   disk3
                                 Physical Store disk1s2
   1:                APFS Volume macOS - 数据            6.4 GB     disk3s1
   2:                APFS Volume Preboot                 310.9 MB   disk3s2
   3:                APFS Volume Recovery                626.4 MB   disk3s3
   4:                APFS Volume VM                      1.1 MB     disk3s4
   5:                APFS Volume macOS                   15.3 GB    disk3s5
   6:              APFS Snapshot com.apple.os.update-... 15.3 GB    disk3s5s1

/dev/disk4 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +127.7 GB   disk4
                                 Physical Store disk2s2
   1:                APFS Volume DOCKER128G              83.1 GB    disk4s1

/dev/disk5 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                                                   *8.0 TB     disk5

/dev/disk6 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +8.3 TB     disk6
                                 Physical Stores disk0, disk5
   1:                APFS Volume FusionDrive             192.4 MB   disk6s1

/dev/disk7 (internal, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                        *31.0 GB    disk7
   1:                        EFI EFI                     209.7 MB   disk7s1
   2:                  Apple_HFS Install macOS Big Sur   13.2 GB    disk7s2
                    (free space)                         134.8 MB   -
   3:       Microsoft Basic Data OC                      398.5 MB   disk7s3
   4:       Microsoft Basic Data CLOVER                  399.5 MB   disk7s4
   5:       Microsoft Basic Data WEPE                    558.9 MB   disk7s5
                    (free space)                         16.1 GB    -
```

至此创建完毕。没有尝试将系统也装在FunsionDrive，目前系统是单独一个磁盘。
