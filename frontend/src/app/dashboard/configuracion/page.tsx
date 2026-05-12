"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import {
  Building2,
  User,
  Bell,
  Shield,
  Smartphone,
  CreditCard,
  Save,
} from "lucide-react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Switch } from "@/components/ui/switch"
import { Separator } from "@/components/ui/separator"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.05,
    },
  },
}

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
}

export default function ConfiguracionPage() {
  const [activeTab, setActiveTab] = useState("empresa")

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="space-y-6"
    >
      {/* Header */}
      <motion.div variants={item}>
        <h1 className="text-3xl font-bold tracking-tight text-foreground">
          Configuracion
        </h1>
        <p className="text-muted-foreground">
          Administra tu cuenta y preferencias
        </p>
      </motion.div>

      {/* Tabs */}
      <motion.div variants={item}>
        <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-6">
          <TabsList className="bg-secondary">
            <TabsTrigger value="empresa" className="data-[state=active]:bg-background gap-2">
              <Building2 className="size-4" />
              Empresa
            </TabsTrigger>
            <TabsTrigger value="perfil" className="data-[state=active]:bg-background gap-2">
              <User className="size-4" />
              Perfil
            </TabsTrigger>
            <TabsTrigger value="notificaciones" className="data-[state=active]:bg-background gap-2">
              <Bell className="size-4" />
              Notificaciones
            </TabsTrigger>
            <TabsTrigger value="seguridad" className="data-[state=active]:bg-background gap-2">
              <Shield className="size-4" />
              Seguridad
            </TabsTrigger>
          </TabsList>

          {/* Empresa Tab */}
          <TabsContent value="empresa" className="space-y-6">
            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="text-foreground">Informacion del Negocio</CardTitle>
                <CardDescription>
                  Datos basicos de tu empresa que apareceran en tus cobros
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="flex items-center gap-6">
                  <Avatar className="h-20 w-20">
                    <AvatarFallback className="bg-primary/20 text-primary text-2xl">
                      ME
                    </AvatarFallback>
                  </Avatar>
                  <div>
                    <Button variant="outline" size="sm">
                      Cambiar logo
                    </Button>
                    <p className="text-xs text-muted-foreground mt-1">
                      JPG, PNG o SVG. Max 1MB.
                    </p>
                  </div>
                </div>
                <Separator />
                <div className="grid gap-4 md:grid-cols-2">
                  <div className="grid gap-2">
                    <Label htmlFor="businessName">Nombre del negocio</Label>
                    <Input id="businessName" defaultValue="Mi Empresa" />
                  </div>
                  <div className="grid gap-2">
                    <Label htmlFor="businessType">Tipo de negocio</Label>
                    <Select defaultValue="salon">
                      <SelectTrigger>
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="salon">Salon de belleza</SelectItem>
                        <SelectItem value="barberia">Barberia</SelectItem>
                        <SelectItem value="estetica">Estetica</SelectItem>
                        <SelectItem value="servicios">Servicios generales</SelectItem>
                        <SelectItem value="otro">Otro</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="grid gap-2">
                    <Label htmlFor="phone">Telefono</Label>
                    <Input id="phone" defaultValue="+506 8888-0000" />
                  </div>
                  <div className="grid gap-2">
                    <Label htmlFor="email">Correo electronico</Label>
                    <Input id="email" type="email" defaultValue="empresa@cobri.app" />
                  </div>
                  <div className="grid gap-2 md:col-span-2">
                    <Label htmlFor="address">Direccion</Label>
                    <Input id="address" placeholder="San Jose, Costa Rica" />
                  </div>
                </div>
                <div className="flex justify-end">
                  <Button className="gap-2">
                    <Save className="size-4" />
                    Guardar cambios
                  </Button>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="text-foreground">Metodos de Pago</CardTitle>
                <CardDescription>
                  Configura los metodos de pago que aceptas
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex items-center justify-between p-4 rounded-lg bg-secondary/50">
                  <div className="flex items-center gap-3">
                    <div className="p-2 rounded-lg bg-primary/10">
                      <Smartphone className="size-5 text-primary" />
                    </div>
                    <div>
                      <p className="font-medium text-foreground">SINPE Movil</p>
                      <p className="text-sm text-muted-foreground">+506 8888-0000</p>
                    </div>
                  </div>
                  <Switch defaultChecked />
                </div>
                <div className="flex items-center justify-between p-4 rounded-lg bg-secondary/50">
                  <div className="flex items-center gap-3">
                    <div className="p-2 rounded-lg bg-success/10">
                      <CreditCard className="size-5 text-success" />
                    </div>
                    <div>
                      <p className="font-medium text-foreground">Efectivo</p>
                      <p className="text-sm text-muted-foreground">Pago en persona</p>
                    </div>
                  </div>
                  <Switch defaultChecked />
                </div>
                <div className="flex items-center justify-between p-4 rounded-lg bg-secondary/50">
                  <div className="flex items-center gap-3">
                    <div className="p-2 rounded-lg bg-accent/10">
                      <CreditCard className="size-5 text-accent" />
                    </div>
                    <div>
                      <p className="font-medium text-foreground">Transferencia Bancaria</p>
                      <p className="text-sm text-muted-foreground">IBAN: CR00-0000-0000</p>
                    </div>
                  </div>
                  <Switch defaultChecked />
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Perfil Tab */}
          <TabsContent value="perfil" className="space-y-6">
            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="text-foreground">Informacion Personal</CardTitle>
                <CardDescription>
                  Tus datos personales de acceso a Cobri
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="flex items-center gap-6">
                  <Avatar className="h-20 w-20">
                    <AvatarFallback className="bg-primary/20 text-primary text-2xl">
                      JD
                    </AvatarFallback>
                  </Avatar>
                  <div>
                    <Button variant="outline" size="sm">
                      Cambiar foto
                    </Button>
                  </div>
                </div>
                <Separator />
                <div className="grid gap-4 md:grid-cols-2">
                  <div className="grid gap-2">
                    <Label htmlFor="firstName">Nombre</Label>
                    <Input id="firstName" defaultValue="Juan" />
                  </div>
                  <div className="grid gap-2">
                    <Label htmlFor="lastName">Apellido</Label>
                    <Input id="lastName" defaultValue="Delgado" />
                  </div>
                  <div className="grid gap-2">
                    <Label htmlFor="userEmail">Correo electronico</Label>
                    <Input id="userEmail" type="email" defaultValue="juan@cobri.app" />
                  </div>
                  <div className="grid gap-2">
                    <Label htmlFor="userPhone">Telefono</Label>
                    <Input id="userPhone" defaultValue="+506 8888-1111" />
                  </div>
                </div>
                <div className="flex justify-end">
                  <Button className="gap-2">
                    <Save className="size-4" />
                    Guardar cambios
                  </Button>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Notificaciones Tab */}
          <TabsContent value="notificaciones" className="space-y-6">
            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="text-foreground">Preferencias de Notificaciones</CardTitle>
                <CardDescription>
                  Elige como quieres recibir alertas y recordatorios
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="space-y-4">
                  <h4 className="text-sm font-medium text-foreground">Pagos</h4>
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm font-medium text-foreground">Pago recibido</p>
                      <p className="text-sm text-muted-foreground">
                        Notificacion cuando un cliente paga
                      </p>
                    </div>
                    <Switch defaultChecked />
                  </div>
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm font-medium text-foreground">Abono recibido</p>
                      <p className="text-sm text-muted-foreground">
                        Notificacion cuando un cliente hace un abono
                      </p>
                    </div>
                    <Switch defaultChecked />
                  </div>
                </div>
                <Separator />
                <div className="space-y-4">
                  <h4 className="text-sm font-medium text-foreground">Cobros</h4>
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm font-medium text-foreground">Cobro por vencer</p>
                      <p className="text-sm text-muted-foreground">
                        Alerta 3 dias antes de vencimiento
                      </p>
                    </div>
                    <Switch defaultChecked />
                  </div>
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm font-medium text-foreground">Cobro vencido</p>
                      <p className="text-sm text-muted-foreground">
                        Alerta cuando un cobro vence
                      </p>
                    </div>
                    <Switch defaultChecked />
                  </div>
                </div>
                <Separator />
                <div className="space-y-4">
                  <h4 className="text-sm font-medium text-foreground">Recordatorios Automaticos</h4>
                  <div className="flex items-center justify-between">
                    <div>
                      <p className="text-sm font-medium text-foreground">Enviar recordatorios por WhatsApp</p>
                      <p className="text-sm text-muted-foreground">
                        Recordatorios automaticos a clientes con deuda
                      </p>
                    </div>
                    <Switch />
                  </div>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          {/* Seguridad Tab */}
          <TabsContent value="seguridad" className="space-y-6">
            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="text-foreground">Cambiar Contrasena</CardTitle>
                <CardDescription>
                  Asegurate de usar una contrasena segura
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid gap-2">
                  <Label htmlFor="currentPassword">Contrasena actual</Label>
                  <Input id="currentPassword" type="password" />
                </div>
                <div className="grid gap-2">
                  <Label htmlFor="newPassword">Nueva contrasena</Label>
                  <Input id="newPassword" type="password" />
                </div>
                <div className="grid gap-2">
                  <Label htmlFor="confirmPassword">Confirmar contrasena</Label>
                  <Input id="confirmPassword" type="password" />
                </div>
                <div className="flex justify-end">
                  <Button className="gap-2">
                    <Save className="size-4" />
                    Actualizar contrasena
                  </Button>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card border-border">
              <CardHeader>
                <CardTitle className="text-foreground">Sesiones Activas</CardTitle>
                <CardDescription>
                  Dispositivos donde has iniciado sesion
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex items-center justify-between p-4 rounded-lg bg-secondary/50">
                  <div>
                    <p className="font-medium text-foreground">Este dispositivo</p>
                    <p className="text-sm text-muted-foreground">
                      Chrome en macOS - San Jose, CR
                    </p>
                  </div>
                  <span className="text-xs text-success">Activo ahora</span>
                </div>
                <div className="flex items-center justify-between p-4 rounded-lg bg-secondary/50">
                  <div>
                    <p className="font-medium text-foreground">iPhone 14</p>
                    <p className="text-sm text-muted-foreground">
                      Safari en iOS - San Jose, CR
                    </p>
                  </div>
                  <Button variant="ghost" size="sm" className="text-destructive">
                    Cerrar sesion
                  </Button>
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card border-border border-destructive/50">
              <CardHeader>
                <CardTitle className="text-destructive">Zona de Peligro</CardTitle>
                <CardDescription>
                  Acciones irreversibles para tu cuenta
                </CardDescription>
              </CardHeader>
              <CardContent>
                <Button variant="destructive" className="gap-2">
                  Eliminar cuenta
                </Button>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </motion.div>
    </motion.div>
  )
}
