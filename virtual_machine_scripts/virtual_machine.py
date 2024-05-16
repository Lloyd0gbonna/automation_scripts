from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import atexit
import ssl
import hashlib

def generate_hash(string):
    # Generate a SHA-256 hash from the given string
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()[:8]  # Return the first 8 characters of the hash as the name

# Disable SSL certificate verification
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
ssl_context.verify_mode = ssl.CERT_NONE

# Connect to vCenter server
si = SmartConnect(host="your_vcenter_ip",
                  user="your_username",
                  pwd="your_password",
                  sslContext=ssl_context)

# Disconnect when done
atexit.register(Disconnect, si)

# Get the content and root folder
content = si.RetrieveContent()
datacenter = content.rootFolder.childEntity[0]
vm_folder = datacenter.vmFolder

# Generate a unique VM name using a hash
vm_name = generate_hash("Unique_VM_Name")

# Create VM configuration
vmx_file = vim.vm.FileInfo(logDirectory=None, snapshotDirectory=None, suspendDirectory=None, vmPathName=None)
config = vim.vm.ConfigSpec(name=vm_name, memoryMB=512, numCPUs=1, files=vmx_file, guestId="ubuntu64")

# Create VM
task = vm_folder.CreateVM_Task(config=config, pool=None, host=None)
print("Creating VM...")

# Wait for task to complete
while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
    continue

if task.info.state == vim.TaskInfo.State.success:
    print("VM created successfully.")
else:
    print("Failed to create VM.")