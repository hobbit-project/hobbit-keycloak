FROM jboss/keycloak:2.4.0.Final

MAINTAINER m.weindel@usu.de

ADD configuration/standalone.xml /opt/jboss/keycloak/standalone/configuration/standalone.xml

RUN mkdir -p /opt/jboss/keycloak/standalone/data/db

VOLUME ["/opt/jboss/keycloak/standalone/data/db"]

ADD themes /opt/jboss/keycloak/themes

ADD hobbit /opt/jboss/keycloak/themes/hobbit/login/hobbit
