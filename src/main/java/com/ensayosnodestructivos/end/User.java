package com.ensayosnodestructivos.end;

import java.util.Date;

/**
 * Created by Abhi on 20 Jan 2018 020.
 */

public class User {
    String nombre;
    String apellido;
    String dni;
    String email;
    String nivel;
    String codigo;
    String fechaalta;
    String fechabaja;
    String activo;
    String telefonomovil;
    String telefonofijo;
    String provincia;
    String cp;
    String pais;
    String usuario;
    String password;

    Date sessionExpiryDate;

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public void setDNI(String dni) {
        this.dni = dni;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setNivel(String nivel) {
        this.nivel = nivel;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public void setFechaalta(String fechaalta) {
        this.fechaalta = fechaalta;
    }

    public void setFechabaja(String fechabaja) {
        this.fechabaja = fechabaja;
    }

    public void setActivo(String activo) {
        this.activo = activo;
    }

    public void setTelefonomovil(String telefonomovil) {
        this.telefonomovil = telefonomovil;
    }

    public void setTelefonofijo(String telefonofijo) {
        this.telefonofijo = telefonofijo;
    }

    public void setProvincia(String provincia) {
        this.provincia = provincia;
    }

    public void setCp(String cp) {
        this.cp = cp;
    }

    public void setPais(String pais) {
        this.pais = pais;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void setSessionExpiryDate(Date sessionExpiryDate) {
        this.sessionExpiryDate = sessionExpiryDate;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public String getDNI() {
        return dni;
    }

    public String getEmail() {
        return email;
    }

    public String getNivel() {
        return nivel;
    }

    public String getCodigo() {
        return codigo;
    }

    public String getFechaalta() { return fechaalta; }

    public String getFechabaja() { return fechabaja; }

    public String getActivo() { return activo; }

    public String getTelefonomovil() { return telefonomovil; }

    public String getTelefonofijo() { return telefonofijo; }

    public String getProvincia() { return provincia; }

    public String getCp() { return cp; }

    public String getPais() { return pais; }

    public String getUsuario() { return usuario; }

    public String getPassword() { return password; }

    public Date getSessionExpiryDate() {
        return sessionExpiryDate;
    }
}
