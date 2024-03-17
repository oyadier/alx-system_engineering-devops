exec { 'increase-fd':
  path => '/bin/'
  command => 'sed -i "s/15/1400" /etc/default/nginx',
}
exec { 'restart':
  path => '/bin/',
  command => 'service nginx restart',
}
	
