Name: harbour-wlan-region
Version: 0.0.2
Release: 0
Summary: Enable 'all' wlan region for Jolla tablet
BuildArch: noarch
Group: System/Base
License: GPLv2
Source0: %{name}-%{version}.tar.gz
URL: https://github.com/tigeli/harbour-wlan-region
BuildRequires: sed
Requires: sed

%description
%{summary}.

%files
%defattr(-,root,root,-)

%prep
%setup -q

%install

%post
/bin/sed -i 's/^#ccode=ALL/ccode=ALL/;s/^ccode=US/#ccode=US/' /system/etc/firmware/bcmdhd_aob.cal
/bin/echo "Please reboot the device to make changes effective!"

%postun
/bin/sed -i 's/^ccode=ALL/#ccode=ALL/;s/^#ccode=US/ccode=US/' /system/etc/firmware/bcmdhd_aob.cal
/bin/echo "Please reboot the device to make changes effective!"
