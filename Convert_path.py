linux_path = "/share/driver/test/001/file.txt"
windows_path = r"C:\share\driver\test\002\file2.txt"

def windows_linux (windows_path):
    extract = windows_path.split("\\")[1:-1]
    extract = "/" + "/".join(extract)
    return extract
    

def linux_windows (linux_path):
    extract = linux_path.split("/")[1:-1]
    extract = "C:" + "/" + "/".join(extract)
    return extract




print(windows_linux(windows_path))
print(linux_windows(linux_path))