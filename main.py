import os
import PySimpleGUI as sg
import rsa
import elgamal as eg
import diffiehelman as dh
import time
from ast import literal_eval

rsa1 = [
    [sg.Text('Prime number 1:', size=(15, 1)), sg.In(key="rsa1_p")],
    [sg.Text('Prime number 2:', size=(15, 1)), sg.In(key="rsa1_q")],
    [sg.Text('E key (optional):', size=(15, 1)), sg.In(key="rsa1_e")],
    [sg.Text('Save as (optional):', size=(15, 1))],
    [sg.Text('Save public key as:', size=(15, 1)), sg.In(key="rsa1_pub"), sg.FileBrowse()],
    [sg.Text('Save private key as:', size=(15, 1)), sg.In(key="rsa1_pri"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Generate Keys', size=(15, 1), key='rsa1_run')],
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
]

eg1 = [
    [sg.Text('Number g:', size=(15, 1)), sg.In(key="eg1_g")],
    [sg.Text('Number x:', size=(15, 1)), sg.In(key="eg1_x")],
    [sg.Text('Number p:', size=(15, 1)), sg.In(key="eg1_p")],
    [sg.Text('Save as (optional):', size=(15, 1))],
    [sg.Text('Save public key as:', size=(15, 1)), sg.In(key="eg1_pub"), sg.FileBrowse()],
    [sg.Text('Save private key as:', size=(15, 1)), sg.In(key="eg1_pri"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Generate Keys', size=(15, 1), key='eg1_run')],
]

eg2_text = [
    [sg.Text('Plaintext:', size=(15, 1)), sg.Multiline(key="eg2_text_in", size=(51,4))],
    [sg.Text('Public key:', size=(15, 1)), sg.In(key="eg2_text_key"), sg.FileBrowse()],
    [sg.Text('Number k:', size=(15, 1)), sg.In(key="eg2_text_k")],
    [sg.Text('')],
    [sg.Button('Encrypt Text', size=(15, 1), key='eg2_text_run')],
    [sg.Text('')],
    [sg.Text('Ciphertext:', size=(15, 1)), sg.Multiline(key="eg2_text_out", size=(51,4))],
]

eg2_file = [
    [sg.Text('Plaintext path:', size=(15, 1)), sg.In(key="eg2_file_in"), sg.FileBrowse()],
    [sg.Text('Public key:', size=(15, 1)), sg.In(key="eg2_file_key"), sg.FileBrowse()],
    [sg.Text('Number k:', size=(15, 1)), sg.In(key="eg2_file_k")],
    [sg.Text('Save as (optional):', size=(15, 1)), sg.In(key="eg2_file_out"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Encrypt Text', size=(15, 1), key='eg2_file_run')],
]

eg3_text = [
    [sg.Text('Ciphertext:', size=(15, 1)), sg.Multiline(key="eg3_text_in", size=(51,4))],
    [sg.Text('Private key:', size=(15, 1)), sg.In(key="eg3_text_key"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Decrypt Text', size=(15, 1), key='eg3_text_run')],
    [sg.Text('')],
    [sg.Text('Plaintext:', size=(15, 1)), sg.Multiline(key="eg3_text_out", size=(51,4))],
]

eg3_file = [
    [sg.Text('Ciphertext path:', size=(15, 1)), sg.In(key="eg3_file_in"), sg.FileBrowse()],
    [sg.Text('Private key:', size=(15, 1)), sg.In(key="eg3_file_key"), sg.FileBrowse()],
    [sg.Text('Save as (optional):', size=(15, 1)), sg.In(key="eg3_file_out"), sg.FileBrowse()],
    [sg.Text('')],
    [sg.Button('Decrypt Text', size=(15, 1), key='eg3_file_run')],
]

dh1 = [
    [sg.Text('Number n:', size=(15, 1)), sg.In(key="dh1_n")],
    [sg.Text('Number g:', size=(15, 1)), sg.In(key="dh1_g")],
    [sg.Text('Number x:', size=(15, 1)), sg.In(key="dh1_x")],
    [sg.Text('Number y:', size=(15, 1)), sg.In(key="dh1_y")],
    [sg.Text('')],
    [sg.Button('Generate Keys', size=(15, 1), key='dh1_run')],
    [sg.Text('')],
    [sg.Text('Key:', size=(15, 1)), sg.Multiline(key="dh1_text_out", size=(51,4))],
]

def pad(content):
    return [[sg.Sizer(0,30)], [sg.Sizer(30,0), sg.Column(content), sg.Sizer(40,0)], [sg.Sizer(0,40)]]

RSA = [[
    sg.TabGroup([[
        sg.Tab('Key', pad(rsa1)),
        sg.Tab('Encrypt', [[
            sg.TabGroup([[
                sg.Tab('From Text', pad(rsa2_text)),
                sg.Tab('From File', pad(rsa2_file)),
            ]])
        ]]),
        sg.Tab('Decrypt', [[
            sg.TabGroup([[
                sg.Tab('From Text', pad(rsa3_text)),
                sg.Tab('From File', pad(rsa3_file)),
            ]])
        ]]),
    ]])
]]

ElGamal = [[
    sg.TabGroup([[
        sg.Tab('Key', pad(eg1)),
        sg.Tab('Encrypt', [[
            sg.TabGroup([[
                sg.Tab('From Text', pad(eg2_text)),
                sg.Tab('From File', pad(eg2_file)),
            ]])
        ]]),
        sg.Tab('Decrypt', [[
            sg.TabGroup([[
                sg.Tab('From Text', pad(eg3_text)),
                sg.Tab('From File', pad(eg3_file)),
            ]])
        ]]),
    ]])
]]

DiffieHelman = [[
    sg.TabGroup([[
        sg.Tab('Key', pad(dh1)),
    ]])
]]

layout = [
    [
        sg.TabGroup([[
            sg.Tab('RSA', RSA),
            sg.Tab('ElGamal', ElGamal),
            sg.Tab('Diffie Helman', DiffieHelman),
        ]])
    ],
    [sg.Frame('Message Output', [[sg.Text('', key='msg', size=(75,5))]])],
]

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
    res = []
    for line in f:
        res.append(int(line))
    f.close()
    return res

window = sg.Window('Public-Key Cryptography', layout)
while True:
    e, v = window.read()

    # RSA KEY
    if e == 'rsa1_run':
        m, n, e, d = rsa.generate_keys(int(v['rsa1_p']), int(v['rsa1_q']), int(v['rsa1_e']))
        if m:
            window['msg'].update(m)
        else:
            pub = str(n) + '\n' + str(e)
            pri = str(n) + '\n' + str(d)
            pub_path = 'rsa_key.pub' if (v['rsa1_pub'] == '') else v['rsa1_pub']
            pri_path = 'rsa_key.pri' if (v['rsa1_pri'] == '') else v['rsa1_pri']
            writeFile(pub, pub_path)
            m = "Public key saved to " + pub_path
            writeFile(pri, pri_path)
            m += "\nPrivate key saved to " + pri_path
            window['msg'].update(m)
    
    # RSA ENCRYPT
    if e == 'rsa2_text_run':
        pt = v['rsa2_text_in'].encode('latin-1')
        keys = readKeys(v['rsa2_text_key'])
        n = keys[0]
        e = keys[1]
        start_time = time.time()
        ct = rsa.encrypt(pt, n, e)
        dur = time.time() - start_time
        window['rsa2_text_out'].update(ct)
        window['msg'].update("Executed in " + str(dur) + " seconds")
    if e == 'rsa2_file_run':
        pt = readText(v['rsa2_file_in'])
        keys = readKeys(v['rsa2_file_key'])
        n = keys[0]
        e = keys[1]
        start_time = time.time()
        ct = rsa.encrypt(pt, n, e)
        dur = time.time() - start_time
        path = 'ciphertext' if (v['rsa2_file_out'] == '') else v['rsa2_file_out']
        writeFile(ct, path)
        window['msg'].update("Executed in " + str(dur) + " seconds\nCiphertext saved to " + path)

    # RSA DECRYPT
    if e == 'rsa3_text_run':
        ct = v['rsa3_text_in'].rstrip('\n')
        keys = readKeys(v['rsa3_text_key'])
        n = keys[0]
        d = keys[1]
        start_time = time.time()
        dur = time.time() - start_time
        pt = rsa.decrypt(ct, n, d).decode('latin-1')
        window['rsa3_text_out'].update(pt)
        window['msg'].update("Executed in " + str(dur) + " seconds")
    if e == 'rsa3_file_run':
        ct = readText(v['rsa3_file_in'])
        keys = readKeys(v['rsa3_file_key'])
        n = keys[0]
        d = keys[1]
        start_time = time.time()
        pt = rsa.decrypt(ct, n, d)
        dur = time.time() - start_time
        path = 'plaintext' if (v['rsa3_file_out'] == '') else v['rsa3_file_out']
        writeFileByte(pt, path)
        window['msg'].update("Executed in " + str(dur) + " seconds\nPlaintext saved to " + path)

    # ELGAMAL KEY
    if e == 'eg1_run':
        pub, pri = eg.get_keys(int(v['eg1_g']), int(v['eg1_x']), int(v['eg1_p']))
        if (pub == 0):
            window['msg'].update("Failed to generate keys; g, x, or p invalid")
        else:
            pub_key = str(pub[0]) + '\n' + str(pub[1]) + '\n' + str(pub[2])
            pri_key = str(pri[0]) + '\n' + str(pri[1])
            pub_path = 'eg_key.pub' if (v['eg1_pub'] == '') else v['eg1_pub']
            pri_path = 'eg_key.pri' if (v['eg1_pri'] == '') else v['eg1_pri']
            writeFile(pub_key, pub_path)
            m = "Public key saved to " + pub_path
            writeFile(pri_key, pri_path)
            m += "\nPrivate key saved to " + pri_path
            window['msg'].update(m)
    
    # ELGAMAL ENCRYPT
    if e == 'eg2_text_run':
        pt = v['eg2_text_in'].encode('latin-1')
        keys = readKeys(v['eg2_text_key'])
        y = keys[0]
        g = keys[1]
        p = keys[2]
        start_time = time.time()
        ct = eg.encrypt(pt, y, g, p, int(v['eg2_text_k']))
        if (ct == 0):
            window['msg'].update("k is not valid")
        else:
            dur = time.time() - start_time
            window['eg2_text_out'].update(ct)
            window['msg'].update("Executed in " + str(dur) + " seconds")
    if e == 'eg2_file_run':
        pt = readText(v['eg2_file_in'])
        keys = readKeys(v['eg2_file_key'])
        y = keys[0]
        g = keys[1]
        p = keys[2]
        start_time = time.time()
        ct = eg.encrypt(pt, y, g, p, int(v['eg2_file_k']))
        if (ct == 0):
            window['msg'].update("k is not valid")
        else:
            dur = time.time() - start_time
            path = 'ciphertext' if (v['eg2_file_out'] == '') else v['eg2_file_out']
            writeFile(ct, path)
            window['msg'].update("Executed in " + str(dur) + " seconds\nCiphertext saved to " + path)

    # ELGAMAL DECRYPT
    if e == 'eg3_text_run':
        ct = literal_eval(v['eg3_text_in'].rstrip('\n'))
        keys = readKeys(v['eg3_text_key'])
        x = keys[0]
        p = keys[1]
        start_time = time.time()
        dur = time.time() - start_time
        pt = eg.decrypt(ct, x, p).decode('latin-1')
        window['eg3_text_out'].update(pt)
        window['msg'].update("Executed in " + str(dur) + " seconds")
    if e == 'eg3_file_run':
        ct = literal_eval(readText(v['eg3_file_in']))
        keys = readKeys(v['eg3_file_key'])
        x = keys[0]
        p = keys[1]
        start_time = time.time()
        pt = eg.decrypt(ct, x, p)
        dur = time.time() - start_time
        path = 'plaintext' if (v['eg3_file_out'] == '') else v['eg3_file_out']
        writeFileByte(pt, path)
        window['msg'].update("Executed in " + str(dur) + " seconds\nPlaintext saved to " + path)

    # ELGAMAL KEY
    if e == 'dh1_run':
        key = dh.get_our_key(int(v['dh1_n']),  int(v['dh1_g']), int(v['dh1_x']), int(v['dh1_y']))
        key = str(key)
        window['dh1_text_out'].update(key)
        m = "Key generated successfully"
        window['msg'].update(m)

    # EXIT
    if e == 'close' or e == sg.WIN_CLOSED:
        break

window.close()