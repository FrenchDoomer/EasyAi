# You should use https://dillinger.io/
with open('easyai/scripts/roop-v1.0/README.html', 'r') as f:
        readme_content = f.read()

METADATA = \
{
        'name': 'Roop',
        'version': '1.0',
        'short_description': 'Take a video and replace the face in it with a face of your choice.',
        'description': readme_content,
        'isdiscontinued': True,
	    'github_link': 'https://github.com/s0md3v/roop'
}