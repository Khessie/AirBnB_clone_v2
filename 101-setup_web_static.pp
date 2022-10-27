package {'nginx':
  ensure => installed
}

exec {'create_dir':
  command  => "sudo mkdir -p /data/web_static/releases/test/",
  provider => shell
}

exec {'create_index':
  command  => "echo '<h1>hello world, this is a test</h1>' | sudo tee /data/web_static/releases/test/index.html",
  provider => shell
}

exec {'create_symlink':
  command  => "sudo ln -sf /data/web_static/releases/test/ /data/web_static/current",
  provider => shell
}

exec {'change_ownership':
  command  => "sudo chown -hR ubuntu:ubuntu /data/",
  provider => shell
}

exec {'add_line':
  command  => "sudo sed -i '11i alias /data/web_static/current/;' /etc/nginx/sites-available/default",
  provider => shell
}

exec {'restart_nginx':
  command  => "sudo service nginx restart",
  provider => shell
}
