# Resolve the occurrence of a 500 error when an HTTP GET request is made to an Apache web server.

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
