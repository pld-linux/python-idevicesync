%define 	module	idevicesync
Summary:	Python synchronization library for iPhone or iPod Touch devices
Name:		python-%{module}
Version:	0.1
Release:	0.1
License:	GPL v2
Group:		Development/Languages/Python
Source0:	http://cgit.sukimashita.com/python-idevicesync.git/snapshot/python-idevicesync-7716f26c6ae788d846252be20695abca19c7bca9.tar.bz2
# Source0-md5:	043f5c4ff9ccddad5d7564db5c5a85e9
URL:		http://cgit.sukimashita.com/python-idevicesync.git/
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-imobiledevice
Requires:	python-modules
Requires:	python-plist
Suggests:	conduit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
python-iphonesync targets to provide a set of classes for use in
applications which want to synchronize data to and from iPhone/iPod
Touch devices.

It is able to retrieve contacts, calendars and bookmarks from a device
and serialize the records into something useful like iCal or vCard
data.

%prep
%setup -qc
mv %{name}-*/* .

%{__sed} -i -e '1s,^#!.*python,#!%{__python},' *.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}
cp -p *.py  $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
