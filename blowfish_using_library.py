from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import binascii

# Khóa mật
key = b'nhom13thuatoanblowfish'

# Văn bản đầu vào
data = b'blowfish13'

# Tạo đối tượng Blowfish cipher
cipher = Blowfish.new(key, Blowfish.MODE_ECB)

# Mã hóa dữ liệu
ciphertext = cipher.encrypt(pad(data, Blowfish.block_size))
print("Ciphertext:", binascii.hexlify(ciphertext))

# Giải mã dữ liệu
decrypted_data = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)
print("Decrypted Data:", decrypted_data.decode())