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

rsa2 = [
    [sg.Text('Input from:', size=(15, 1)), sg.Combo(['text', 'file'], default_value='text', key="rsa2_type", size=(20,1))],
    [sg.Text('Plaintext:', size=(15, 1)), sg.Multiline(key="rsa2_in", size=(51,4))],
    [sg.Text('Plaintext path:', size=(15, 1)), sg.In(key="rsa2_in_path"), sg.FileBrowse()],
    [sg.Text('Public key:', size=(15, 1)), sg.In(key="rsa2_key_path"), sg.FileBrowse()],
    [sg.Text('Ciphertext:', size=(15, 1)), sg.Multiline(key="rsa2_out", size=(51,4))],
    [sg.Text('Save as (optional):', size=(15, 1)), sg.In(key="rsa2_out_path"), sg.FileBrowse()],
    [sg.Text('')],
    [
        sg.Button('Encrypt Text', size=(15, 1), key='rsa2_run'),
        sg.Button('Save Ciphertext', size=(15, 1), key='rsa2_save')
    ],
    [sg.Text('_'*75)],
    [sg.Text('Output Message')],
    [sg.Text('', key='rsa2_msg', size=(65,3))],
]

rsa3 = [
    [sg.Text('Input from:', size=(15, 1)), sg.Combo(['text', 'file'], default_value='text', key="rsa3_type", size=(20,1))],
    [sg.Text('Ciphertext:', size=(15, 1)), sg.Multiline(key="rsa3_in", size=(51,4))],
    [sg.Text('Ciphertext path:', size=(15, 1)), sg.In(key="rsa3_in_path"), sg.FileBrowse()],
    [sg.Text('Private key:', size=(15, 1)), sg.In(key="rsa3_key_path"), sg.FileBrowse()],
    [sg.Text('Plaintext:', size=(15, 1)), sg.Multiline(key="rsa3_out", size=(51,4))],
    [sg.Text('Save as (optional):', size=(15, 1)), sg.In(key="rsa3_out_path"), sg.FileBrowse()],
    [sg.Text('')],
    [
        sg.Button('Decrypt Text', size=(15, 1), key='rsa3_run'),
        sg.Button('Save Plaintext', size=(15, 1), key='rsa3_save')
    ],
    [sg.Text('_'*75)],
    [sg.Text('Output Message')],
    [sg.Text('', key='rsa3_msg', size=(65,3))],
]

def pad(content):
    return [[sg.Sizer(0,30)], [sg.Sizer(30,0), sg.Column(content), sg.Sizer(40,0)], [sg.Sizer(0,40)]]

layout = [[
    sg.TabGroup([[
        sg.Tab('RSA Key',     pad(rsa1)),
        sg.Tab('RSA Encrypt', pad(rsa2)),
        sg.Tab('RSA Decrypt', pad(rsa3)),
    ]])
]]

def getRelPath(path):
    return os.path.relpath(path, os.path.abspath(os.getcwd()))

def writeFile(msg, path):
    f = open(path, "w")
    f.write(msg)
    f.close()

def readFile(path):
    f = open(path, "r")
    msg = f.read()
    f.close()
    return msg

window = sg.Window('Public-Key Cryptography', layout)
while True:
    e, v = window.read()

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

    if e == 'close' or e == sg.WIN_CLOSED:
        break

window.close()