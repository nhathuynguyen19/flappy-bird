from setuptools import setup, find_packages

setup(
    name='flappy-bird',  # Thay 'my_project' bằng tên dự án
    version='0.1.0',  # Phiên bản dự án (có thể thay đổi sau mỗi lần release)
    packages=find_packages(),  # Tự động tìm tất cả các thư mục chứa mã nguồn
    install_requires=[
        # Danh sách các thư viện phụ thuộc của dự án, ví dụ:
        # 'requests', 'numpy',
        'pygame',
    ],
    entry_points={
        'console_scripts': [
            # Nếu dự án có entry point, thêm vào đây
            # 'my_project = my_project.main:main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='nhathuynguyen19',  # Tên tác giả
    author_email='huythcsthuyphuong73@gmail.com',  # Email tác giả
    url='',  # URL của dự án (nếu có)
    license='MIT',  # Giấy phép của dự án
)
