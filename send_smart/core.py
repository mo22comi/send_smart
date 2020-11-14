import socket
import re
from subprocess import Popen, PIPE
import consts
from html import Html
from mail import Mail


def res_cmd_linefeed(cmd):
    return Popen(cmd, stdout=PIPE, shell=True).stdout.readlines()


def decode_output(output):
    if len(output) == 1:
        return output[0].decode('utf-8').rstrip('\n').strip()
    elif len(output) > 1:
        output_list = []
        for x in output:
            output_list.append(x.decode('utf-8').rstrip('\n').strip())
        return output_list


def disk_usage():
    usage_output = res_cmd_linefeed(consts.DF_CMD)
    dec_output = decode_output(usage_output)
    usage = re.search(r'\d{1,3}%', dec_output).group()
    usage_str = '{} 使用率：{}'.format(dec_output.split(' ')[0], usage)

    return usage_str


def disk_info():
    info_list = res_cmd_linefeed(consts.DISK_INFO_CMD)
    dec_list = decode_output(info_list)
    disk_list = []
    for i in range(len(dec_list)):
        disk_str = 'Disk {} : {}'.format(str(i + 1), dec_list[i])
        disk_list.append(disk_str)

    return disk_list


def smart_info():
    res_smart = res_cmd_linefeed(consts.SMART_LIST_CMD)
    dec_output = [x.rstrip('\n') for x in decode_output(res_smart)]
    smart_list = []

    for file in dec_output:
        if '.info' in file:
            cmd = consts.SMART_INFO_CMD + file
            res = res_cmd_linefeed(cmd)
            dec = decode_output(res)
            smart_list.append(dec)
    return smart_list


def send_smart():
    hostname = socket.gethostname()
    mail_info = consts.MAIL_INFO.copy()
    html_contents = Html(
        usage=disk_usage(),
        disks=disk_info(),
        smart=smart_info(),
        columns=consts.SMART_TABLE_COLUMN,
        template_path=consts.TEMPLATE_PATH
    )
    subject = '{} {} from {}'.format(consts.NAS_NAME, consts.MAIL_SUBJECT, hostname)
    body = html_contents.build_html()
    mail_dict = {
        'subject': subject,
        'body': body
    }
    mailer = Mail(mail_info)
    msg = mailer.create_message(mail_dict)
    mailer.send_mail(msg)


if __name__ == '__main__':
    send_smart()
