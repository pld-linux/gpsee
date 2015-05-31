#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests

Summary:	General Purpose Spidermonkey Embedding Ecosystem
Name:		gpsee
Version:	0.2.1
Release:	0.1
License:	MPL 1.1/GPL 2.0/LGPL 2.1
Group:		Applications
Source0:	https://bitbucket.org/wesgarland/gpsee/get/a32272516d00.tar.bz2
# Source0-md5:	9d1976e440e5b7c1a50f9e00d565cd0d
URL:		http://gpsee.blogspot.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
What is GPSEE?
- a platform for developing and running ServerSide JavaScript CommonJS
  programs
- a general-purpose C API for embedding SpiderMonkey + CommonJS
- a general-purpose C API for adding interoperability between JSAPI
  projects licensed under the exact same terms as SpiderMonkey (MPL 1.1,
  GPLv2, LGPL 2.1)

%prep
%setup -qc
mv wesgarland-gpsee-*/* .

%build
# NOTE: not autoconf configure
./configure \
  --enable-curl \
  --with-build=RELEASE \
  --with-cc="%{__cc}" \
  --with-cxx="%{__cxx}" \
  --prefix=%{_prefix}

# fix configure not handling spaces before enabling with *flags options
#  --with-cppflags="%{rpmcppflags}" \
#  --with-cxxflags="%{rpmcxxflags}" \
#  --with-ldflags="%{rpmldflags}" \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
