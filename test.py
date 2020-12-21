import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
      
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'FT5ORq_GSegAAAAAAAAAAfwo0guCe6unk3GKbipkffYqXDwtDyWfQa9zxLohErh5'
    transferData = TransferData(access_token)

    fromd = input('Which Folder Do You Want To Upload To Your Dropbox ?')

    file_from = fromd
    file_to = '/users/kalravmineshbhatt/Dropbox/' 

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()