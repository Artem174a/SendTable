import os

from html_creator import HtmlBuilder, HTML_VIEW
from mail import Mailing


def create_html():
    with open(os.path.join(HTML_VIEW, 'default.html'), 'r') as file:
        html_builder = HtmlBuilder(file.read())

    html_content = html_builder \
        .set_title("A Simple Responsive HTML Email") \
        .set_body_head_title("Your Head Title") \
        .set_body_middle_text("Your Middle Text Here") \
        .set_body_bottom_text("Your Bottom Text Here") \
        .build()

    print(html_content)

    return html_content


if __name__ == "__main__":
    mail_app = Mailing('artem174a@yandex.ru', 'lfmijajpyogsgjzu')
    mail_app.run_mailing(
        subject="Тема",
        body="Отправка файла",
        recipients=['artem174a@yandex.ru'],
        file_path='test_file.txt',
        html_message=create_html()
    )
