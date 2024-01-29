# Puppet Manifest for creating a file in /tmp
# File path: /tmp/school
# File permission: 0744
# File owner: www-data
# File group: www-data
# File content: I love Puppet

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
