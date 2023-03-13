import os

class Event:
    def __init__(self, timestamp, func) -> None:
        self._timestamp = timestamp
        self._func = func

HOSTS = {
    "hub": "SHA=0cb07f5bff5865ca5268dc1a5cc8599a7a4e6894d4ee954913016cc699b84e3f",
    "centos": "SHA=7254f21cc164054e92c513abf4079d0671fd43341cfaf40fedad6bbe00dbdd46",
    "debian": "SHA=f373628225ce71586ae38a844c63a6da1fbe124bb4770b805c1bc4a133a3482e",
    "rhel": "SHA=15580be79bd3b71c1b7e0cddf38ad84c0228cefdfc8282ab7f3207fa6dbaf228",
    "ubuntu": "SHA=6c1baabfc29d73409938f0be462bfecd8492b5a47f475c78c8f1817f959053ba",
}

def main():
    for hostname, hostkey in HOSTS.items():
        for dirpath, _, filenames in os.walk(hostname):
            if "report_dumps" in dirpath:
                continue

            for filename in filenames:
                if "classes" in filename:
                    header = "name,meta\r\n"
                elif "execution_log" in filename:
                    header = "promise_hash,policy_filename,release_id,promise_outcome,namespace,bundle,promise_type,promiser,stack_path,handle,promisee,messages,line_number,policy_file_hash\r\n"
                elif "lastseen" in filename:
                    header = "direction,hostkey,address,interval,lastseen\r\n"
                elif "patch" in filename:
                    header = "name,version,architecture,status\r\n"
                elif "software" in filename:
                    header = "name,version,architecture\r\n"
                elif "variables" in filename:
                    header = "namespace,bundle,name,type,value,meta\r\n"
                else:
                    assert(False)

                with open(os.path.join(dirpath, filename), "r") as f:
                    content = f.read()

                with open(os.path.join(dirpath, filename), "w") as f:
                    f.write(header)
                    f.write(content)



if __name__ == "__main__":
    main()
