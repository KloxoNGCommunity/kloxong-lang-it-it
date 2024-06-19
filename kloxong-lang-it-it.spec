%define kloxo /usr/local/lxlabs/kloxo/httpdocs/lang
%define productname kloxo-lang
%define packagename it-it
%define sourcename it-it
%define timestamp 2013031825

Name: %{productname}-%{packagename}
Summary: Kloxo IT-IT language
Version: 6.5.0.f
Release: 2.kng%{?dist}
License: GPL
Group: Applications/Internet

Source0: %{name}-%{version}-%{timestamp}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

Obsoletes: kloxomr-lang-it-it

%description
Kloxo PL-PL language

%prep
%setup -q -n %{name}-%{version}-%{timestamp}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}/%{packagename}
%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}/%{packagename}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,lxlabs,lxlabs,755)
%{kloxo}/%{packagename}

%changelog
* Wed Jun 19 2024 John Parnell Pierce <john@luckytanuki.com>
- Change product name back to Kloxo

* Mon Jan 29 2018 John Parnell Pierce <john@luckytanuki.com> 
- change product name to kloxong
- add obsolete for kloxomr 

* Wed Jun 26 2013 Mustafa Ramadhan <mustafa@bigraf.com> - 6.5.0.f.2013031825-1.mr
- compile Kloxo-MR language (only en-us including Kloxo-MR package)
- constribute by ynuyasha <antonio.falzarano@gmail.com>
