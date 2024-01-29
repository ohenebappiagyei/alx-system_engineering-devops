# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create custom HTTP header response configuration
file { '/etc/nginx/sites-available/custom_header':
  ensure  => present,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;
                root /var/www/html;
                index index.html index.htm index.nginx-debian.html;
                server_name _;
                add_header X-Served-By $hostname;
                location / {
                        try_files \$uri \$uri/ =404;
                }
                if (\$request_filename ~ redirect_me){
                        rewrite ^ https://th3-gr00t.tk/ permanent;
                }
                error_page 404 /error_404.html;
                location = /error_404.html {
                        internal;
                }
              }",
}

# Enable the custom header response configuration
file { '/etc/nginx/sites-enabled/custom_header':
  ensure => link,
  target => '/etc/nginx/sites-available/custom_header',
}

# Restart Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/custom_header'],
}

