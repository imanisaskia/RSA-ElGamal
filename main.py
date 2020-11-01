import os
import PySimpleGUI as sg
import rsa

rsa1 = [
    [sg.Text('Prime number 1:', size=(15, 1)), sg.In(key="rsa1_p")],
    [sg.Text('Prime number 2:', size=(15, 1)), sg.In(key="rsa1_q")],
    [sg.Text('E key (optional):', size=(15, 1)), sg.In(key="rsa1_e")],
    [sg.Text('Save as (optional):', size=(15, 1))],
    [sg.Text('Save public key as:', size=(15, 1)), sg.In(key="rsa1_pub"), sg.FileBrowse()],
    [sg.Text('Save private key as:', size=(15, 1)), sg.In(key="rsa1_pri"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Generate Keys', size=(15, 1), key='rsa1_run')],
    [sg.Text('_'*75)],
    [sg.Text('Output Message')],
    [sg.Text('', key='rsa1_msg', size=(65,3))],
]

rsa2_text = [
    [sg.Text('Plaintext:', size=(15, 1)), sg.Multiline(key="rsa2_text_in", size=(51,4))],
    [sg.Text('Public key:', size=(15, 1)), sg.In(key="rsa2_text_key"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Encrypt Text', size=(15, 1), key='rsa2_text_run')],
    [sg.Text('')],
    [sg.Text('Ciphertext:', size=(15, 1)), sg.Multiline(key="rsa2_text_out", size=(51,4))],
]

rsa2_file = [
    [sg.Text('Plaintext path:', size=(15, 1)), sg.In(key="rsa2_file_in"), sg.FileBrowse()],
    [sg.Text('Public key:', size=(15, 1)), sg.In(key="rsa2_file_key"), sg.FileBrowse()],
    [sg.Text('Save as (optional):', size=(15, 1)), sg.In(key="rsa2_file_out"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Encrypt Text', size=(15, 1), key='rsa2_file_run')],
    [sg.Text('_'*75)],
    [sg.Text('Output Message')],
    [sg.Text('', key='rsa2_file_msg', size=(65,3))],
]

rsa3_text = [
    [sg.Text('Ciphertext:', size=(15, 1)), sg.Multiline(key="rsa3_text_in", size=(51,4))],
    [sg.Text('Private key:', size=(15, 1)), sg.In(key="rsa3_text_key"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Decrypt Text', size=(15, 1), key='rsa3_text_run')],
    [sg.Text('')],
    [sg.Text('Plaintext:', size=(15, 1)), sg.Multiline(key="rsa3_text_out", size=(51,4))],
]

rsa3_file = [
    [sg.Text('Ciphertext path:', size=(15, 1)), sg.In(key="rsa3_file_in"), sg.FileBrowse()],
    [sg.Text('Private key:', size=(15, 1)), sg.In(key="rsa3_file_key"), sg.FileBrowse()],
    [sg.Text('Save as (optional):', size=(15, 1)), sg.In(key="rsa3_file_out"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Decrypt Text', size=(15, 1), key='rsa3_file_run')],
    [sg.Text('_'*75)],
    [sg.Text('Output Message')],
    [sg.Text('', key='rsa3_file_msg', size=(65,3))],
]

def pad(content):
    return [[sg.Sizer(0,30)], [sg.Sizer(30,0), sg.Column(content), sg.Sizer(40,0)], [sg.Sizer(0,40)]]

rsa2 = [[
    sg.TabGroup([[
        sg.Tab('From Text', pad(rsa2_text)),
        sg.Tab('From File', pad(rsa2_file)),
    ]])
]]

rsa3 = [[
    sg.TabGroup([[
        sg.Tab('From Text', pad(rsa3_text)),
        sg.Tab('From File', pad(rsa3_file)),
    ]])
]]

layout = [[
    sg.TabGroup([[
        sg.Tab('RSA Key',     pad(rsa1)),
        sg.Tab('RSA Encrypt', rsa2),
        sg.Tab('RSA Decrypt', rsa3),
    ]])
]]

def writeFile(msg, path):
    f = open(path, "w")
    f.write(msg)
    f.close()

def writeFileByte(msg_bytes, path):
    f = open(path, "wb")
    f.write(msg_bytes)
    f.close()

def readText(path):
    f = open(path, "rb")
    msg = f.read()
    f.close()
    return msg

def readKeys(path):
    f = open(path, "r")
    v1 = int(f.readline())
    v2 = int(f.readline())
    f.close()
    return v1, v2

window = sg.Window('Public-Key Cryptography', layout)
while True:
    e, v = window.read()

    # RSA KEY
    if e == 'rsa1_run':
        m, n, e, d = rsa.generate_keys(int(v['rsa1_p']), int(v['rsa1_q']), int(v['rsa1_e']))
        if m:
            window['rsa1_msg'].update(m)
        else:
            pub = str(n) + '\n' + str(e)
            pri = str(n) + '\n' + str(d)
            pub_path = 'key.pub' if (v['rsa1_pub'] == '') else v['rsa1_pub']
            pri_path = 'key.pri' if (v['rsa1_pri'] == '') else v['rsa1_pri']
            writeFile(pub, pub_path)
            m = "Public key saved to " + pub_path
            writeFile(pri, pri_path)
            m += "\nPrivate key saved to " + pri_path
            window['rsa1_msg'].update(m)
    
    # RSA ENCRYPT
    if e == 'rsa2_text_run':
        pt = v['rsa2_text_in'].encode('latin-1')
        n, e = readKeys(v['rsa2_text_key'])
        ct = rsa.encrypt(pt, n, e)
        window['rsa2_text_out'].update(ct)        
    if e == 'rsa2_file_run':
        pt = readText(v['rsa2_file_in'])
        n, e = readKeys(v['rsa2_file_key'])
        ct = rsa.encrypt(pt, n, e)
        path = 'ciphertext' if (v['rsa2_file_out'] == '') else v['rsa2_file_out']
        writeFile(ct, path)
        window['rsa2_file_msg'].update("Ciphertext saved to " + path)

    # RSA DECRYPT
    if e == 'rsa3_text_run':
        ct = v['rsa3_text_in'].rstrip('\n')
        n, d = readKeys(v['rsa3_text_key'])
        pt = rsa.decrypt(ct, n, d).decode('latin-1')
        window['rsa3_text_out'].update(pt)
    if e == 'rsa3_file_run':
        ct = readText(v['rsa3_file_in'])
        n, d = readKeys(v['rsa3_file_key'])
        pt = rsa.decrypt(ct, n, d)
        path = 'plaintext' if (v['rsa3_file_out'] == '') else v['rsa3_file_out']
        writeFileByte(pt, path)
        window['rsa3_file_msg'].update("Plaintext saved to " + path)

    # EXIT
    if e == 'close' or e == sg.WIN_CLOSED:
        break

window.close()