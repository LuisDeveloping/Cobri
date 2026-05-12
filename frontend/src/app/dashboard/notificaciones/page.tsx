"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import {
  Search,
  Bell,
  MessageSquare,
  Check,
  X,
  Clock,
  AlertCircle,
  MoreHorizontal,
} from "lucide-react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"

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

// Mock data
const notifications = [
  {
    id: 1,
    type: "payment",
    title: "Pago recibido",
    message: "Maria Garcia pago 35,000 CRC por servicio de maquillaje",
    time: "Hace 5 min",
    read: false,
  },
  {
    id: 2,
    type: "reminder",
    title: "Recordatorio enviado",
    message: "Se envio recordatorio de pago a Carlos Rodriguez (15,000 CRC)",
    time: "Hace 30 min",
    read: false,
  },
  {
    id: 3,
    type: "overdue",
    title: "Cobro vencido",
    message: "El cobro COB-005 de Patricia Lopez esta vencido (120,000 CRC)",
    time: "Hace 2 horas",
    read: false,
  },
  {
    id: 4,
    type: "payment",
    title: "Abono recibido",
    message: "Luis Fernandez realizo un abono de 35,000 CRC",
    time: "Hace 3 horas",
    read: true,
  },
  {
    id: 5,
    type: "system",
    title: "Nuevo cliente",
    message: "Se agrego el cliente Sofia Vargas a tu cartera",
    time: "Ayer",
    read: true,
  },
  {
    id: 6,
    type: "overdue",
    title: "Cobro vencido",
    message: "El cobro COB-006 de Roberto Sanchez vencio hace 14 dias",
    time: "Ayer",
    read: true,
  },
  {
    id: 7,
    type: "reminder",
    title: "Recordatorio programado",
    message: "Se enviara recordatorio a Miguel Torres manana",
    time: "Hace 2 dias",
    read: true,
  },
]

function getNotificationIcon(type: string) {
  switch (type) {
    case "payment":
      return { icon: Check, color: "text-success", bg: "bg-success/10" }
    case "reminder":
      return { icon: MessageSquare, color: "text-primary", bg: "bg-primary/10" }
    case "overdue":
      return { icon: AlertCircle, color: "text-destructive", bg: "bg-destructive/10" }
    case "system":
      return { icon: Bell, color: "text-accent", bg: "bg-accent/10" }
    default:
      return { icon: Bell, color: "text-muted-foreground", bg: "bg-muted" }
  }
}

export default function NotificacionesPage() {
  const [activeTab, setActiveTab] = useState("all")
  const [notificationsList, setNotificationsList] = useState(notifications)

  const unreadCount = notificationsList.filter((n) => !n.read).length

  const filteredNotifications = notificationsList.filter((notification) => {
    if (activeTab === "all") return true
    if (activeTab === "unread") return !notification.read
    return notification.type === activeTab
  })

  const markAsRead = (id: number) => {
    setNotificationsList((prev) =>
      prev.map((n) => (n.id === id ? { ...n, read: true } : n))
    )
  }

  const markAllAsRead = () => {
    setNotificationsList((prev) => prev.map((n) => ({ ...n, read: true })))
  }

  return (
    <motion.div
      variants={container}
      initial="hidden"
      animate="show"
      className="space-y-6"
    >
      {/* Header */}
      <motion.div variants={item} className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-foreground">
            Notificaciones
          </h1>
          <p className="text-muted-foreground">
            Mantente al dia con la actividad de tus cobros
          </p>
        </div>
        {unreadCount > 0 && (
          <Button variant="outline" onClick={markAllAsRead}>
            Marcar todo como leido
          </Button>
        )}
      </motion.div>

      {/* Stats */}
      <motion.div variants={item} className="grid gap-4 md:grid-cols-4">
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Sin Leer
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-primary">{unreadCount}</div>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Pagos
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-success">
              {notificationsList.filter((n) => n.type === "payment").length}
            </div>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Recordatorios
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-primary">
              {notificationsList.filter((n) => n.type === "reminder").length}
            </div>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Alertas
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-destructive">
              {notificationsList.filter((n) => n.type === "overdue").length}
            </div>
          </CardContent>
        </Card>
      </motion.div>

      {/* Tabs */}
      <motion.div variants={item}>
        <Tabs value={activeTab} onValueChange={setActiveTab}>
          <TabsList className="bg-secondary">
            <TabsTrigger value="all" className="data-[state=active]:bg-background">
              Todas
            </TabsTrigger>
            <TabsTrigger value="unread" className="data-[state=active]:bg-background">
              Sin leer
              {unreadCount > 0 && (
                <Badge variant="secondary" className="ml-2 bg-primary/20 text-primary">
                  {unreadCount}
                </Badge>
              )}
            </TabsTrigger>
            <TabsTrigger value="payment" className="data-[state=active]:bg-background">
              Pagos
            </TabsTrigger>
            <TabsTrigger value="overdue" className="data-[state=active]:bg-background">
              Alertas
            </TabsTrigger>
          </TabsList>

          <div className="mt-4">
            <Card className="bg-card border-border">
              <CardContent className="p-0">
                <div className="divide-y divide-border">
                  {filteredNotifications.length === 0 ? (
                    <div className="p-8 text-center text-muted-foreground">
                      No hay notificaciones
                    </div>
                  ) : (
                    filteredNotifications.map((notification) => {
                      const { icon: Icon, color, bg } = getNotificationIcon(notification.type)

                      return (
                        <motion.div
                          key={notification.id}
                          initial={{ opacity: 0 }}
                          animate={{ opacity: 1 }}
                          className={`flex items-start gap-4 p-4 hover:bg-secondary/50 transition-colors ${
                            !notification.read ? "bg-primary/5" : ""
                          }`}
                        >
                          <div className={`p-2 rounded-lg ${bg} shrink-0`}>
                            <Icon className={`size-5 ${color}`} />
                          </div>
                          <div className="flex-1 min-w-0">
                            <div className="flex items-center gap-2">
                              <span className="font-medium text-foreground">
                                {notification.title}
                              </span>
                              {!notification.read && (
                                <span className="h-2 w-2 rounded-full bg-primary shrink-0" />
                              )}
                            </div>
                            <p className="text-sm text-muted-foreground mt-0.5">
                              {notification.message}
                            </p>
                            <p className="text-xs text-muted-foreground mt-1">
                              {notification.time}
                            </p>
                          </div>
                          <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                              <Button variant="ghost" size="icon" className="size-8 shrink-0">
                                <MoreHorizontal className="size-4" />
                              </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent align="end">
                              {!notification.read && (
                                <DropdownMenuItem onClick={() => markAsRead(notification.id)}>
                                  <Check className="mr-2 size-4" />
                                  Marcar como leido
                                </DropdownMenuItem>
                              )}
                              <DropdownMenuItem className="text-destructive">
                                <X className="mr-2 size-4" />
                                Eliminar
                              </DropdownMenuItem>
                            </DropdownMenuContent>
                          </DropdownMenu>
                        </motion.div>
                      )
                    })
                  )}
                </div>
              </CardContent>
            </Card>
          </div>
        </Tabs>
      </motion.div>
    </motion.div>
  )
}
