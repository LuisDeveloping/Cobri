"use client"

import { useState } from "react"
import { motion } from "framer-motion"
import {
  Search,
  Plus,
  MoreHorizontal,
  Phone,
  Mail,
  Filter,
  ChevronDown,
  Eye,
  Pencil,
  Trash2,
  MessageSquare,
} from "lucide-react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Badge } from "@/components/ui/badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { Label } from "@/components/ui/label"
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

// Mock data
const clients = [
  {
    id: 1,
    name: "Maria Garcia",
    phone: "+506 8888-1234",
    email: "maria@email.com",
    totalDebt: 0,
    totalPaid: 150000,
    status: "active",
    lastPayment: "2024-01-15",
  },
  {
    id: 2,
    name: "Carlos Rodriguez",
    phone: "+506 8888-5678",
    email: "carlos@email.com",
    totalDebt: 45000,
    totalPaid: 85000,
    status: "pending",
    lastPayment: "2024-01-10",
  },
  {
    id: 3,
    name: "Ana Martinez",
    phone: "+506 8888-9012",
    email: "ana@email.com",
    totalDebt: 0,
    totalPaid: 220000,
    status: "active",
    lastPayment: "2024-01-14",
  },
  {
    id: 4,
    name: "Luis Fernandez",
    phone: "+506 8888-3456",
    email: "luis@email.com",
    totalDebt: 125000,
    totalPaid: 50000,
    status: "overdue",
    lastPayment: "2023-12-20",
  },
  {
    id: 5,
    name: "Patricia Lopez",
    phone: "+506 8888-7890",
    email: "patricia@email.com",
    totalDebt: 85000,
    totalPaid: 120000,
    status: "pending",
    lastPayment: "2024-01-05",
  },
  {
    id: 6,
    name: "Roberto Sanchez",
    phone: "+506 8888-2345",
    email: "roberto@email.com",
    totalDebt: 200000,
    totalPaid: 0,
    status: "overdue",
    lastPayment: null,
  },
  {
    id: 7,
    name: "Sofia Vargas",
    phone: "+506 8888-6789",
    email: "sofia@email.com",
    totalDebt: 0,
    totalPaid: 180000,
    status: "active",
    lastPayment: "2024-01-16",
  },
  {
    id: 8,
    name: "Miguel Torres",
    phone: "+506 8888-0123",
    email: "miguel@email.com",
    totalDebt: 30000,
    totalPaid: 95000,
    status: "pending",
    lastPayment: "2024-01-12",
  },
]

function formatCurrency(amount: number) {
  return new Intl.NumberFormat("es-CR", {
    style: "currency",
    currency: "CRC",
    minimumFractionDigits: 0,
  }).format(amount)
}

function formatDate(dateString: string | null) {
  if (!dateString) return "Sin pagos"
  return new Date(dateString).toLocaleDateString("es-CR", {
    day: "numeric",
    month: "short",
    year: "numeric",
  })
}

function getStatusBadge(status: string) {
  switch (status) {
    case "active":
      return (
        <Badge className="bg-success/20 text-success hover:bg-success/30">
          Al dia
        </Badge>
      )
    case "pending":
      return (
        <Badge className="bg-warning/20 text-warning hover:bg-warning/30">
          Pendiente
        </Badge>
      )
    case "overdue":
      return (
        <Badge className="bg-destructive/20 text-destructive hover:bg-destructive/30">
          Vencido
        </Badge>
      )
    default:
      return <Badge variant="outline">Desconocido</Badge>
  }
}

export default function ClientesPage() {
  const [searchQuery, setSearchQuery] = useState("")
  const [statusFilter, setStatusFilter] = useState<string>("all")
  const [isDialogOpen, setIsDialogOpen] = useState(false)

  const filteredClients = clients.filter((client) => {
    const matchesSearch =
      client.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      client.phone.includes(searchQuery) ||
      client.email.toLowerCase().includes(searchQuery.toLowerCase())

    const matchesStatus =
      statusFilter === "all" || client.status === statusFilter

    return matchesSearch && matchesStatus
  })

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
            Clientes
          </h1>
          <p className="text-muted-foreground">
            Gestiona tu cartera de clientes y su historial
          </p>
        </div>
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogTrigger asChild>
            <Button className="gap-2">
              <Plus className="size-4" />
              Nuevo Cliente
            </Button>
          </DialogTrigger>
          <DialogContent className="sm:max-w-[425px]">
            <DialogHeader>
              <DialogTitle>Agregar Cliente</DialogTitle>
              <DialogDescription>
                Agrega un nuevo cliente a tu cartera. Completa los datos basicos.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <div className="grid gap-2">
                <Label htmlFor="name">Nombre completo</Label>
                <Input id="name" placeholder="Ej: Maria Garcia" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="phone">Telefono</Label>
                <Input id="phone" placeholder="+506 8888-0000" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="email">Correo electronico</Label>
                <Input id="email" type="email" placeholder="cliente@email.com" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="notes">Notas (opcional)</Label>
                <Input id="notes" placeholder="Notas adicionales..." />
              </div>
            </div>
            <DialogFooter>
              <Button variant="outline" onClick={() => setIsDialogOpen(false)}>
                Cancelar
              </Button>
              <Button onClick={() => setIsDialogOpen(false)}>
                Guardar Cliente
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>
      </motion.div>

      {/* Stats Cards */}
      <motion.div variants={item} className="grid gap-4 md:grid-cols-3">
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Total Clientes
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-foreground">
              {clients.length}
            </div>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Clientes al Dia
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-success">
              {clients.filter((c) => c.status === "active").length}
            </div>
          </CardContent>
        </Card>
        <Card className="bg-card border-border">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">
              Con Deuda
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-warning">
              {clients.filter((c) => c.totalDebt > 0).length}
            </div>
          </CardContent>
        </Card>
      </motion.div>

      {/* Filters */}
      <motion.div variants={item} className="flex flex-col gap-4 md:flex-row md:items-center">
        <div className="relative flex-1 max-w-sm">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-muted-foreground" />
          <Input
            placeholder="Buscar por nombre, telefono o email..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="pl-9"
          />
        </div>
        <Select value={statusFilter} onValueChange={setStatusFilter}>
          <SelectTrigger className="w-[180px]">
            <Filter className="size-4 mr-2" />
            <SelectValue placeholder="Estado" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">Todos</SelectItem>
            <SelectItem value="active">Al dia</SelectItem>
            <SelectItem value="pending">Pendiente</SelectItem>
            <SelectItem value="overdue">Vencido</SelectItem>
          </SelectContent>
        </Select>
      </motion.div>

      {/* Table */}
      <motion.div variants={item}>
        <Card className="bg-card border-border">
          <CardContent className="p-0">
            <Table>
              <TableHeader>
                <TableRow className="border-border hover:bg-transparent">
                  <TableHead className="text-muted-foreground">Cliente</TableHead>
                  <TableHead className="text-muted-foreground">Contacto</TableHead>
                  <TableHead className="text-muted-foreground">Deuda</TableHead>
                  <TableHead className="text-muted-foreground">Pagado</TableHead>
                  <TableHead className="text-muted-foreground">Estado</TableHead>
                  <TableHead className="text-muted-foreground">Ultimo Pago</TableHead>
                  <TableHead className="text-muted-foreground w-[50px]"></TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {filteredClients.map((client) => (
                  <TableRow
                    key={client.id}
                    className="border-border hover:bg-secondary/50"
                  >
                    <TableCell>
                      <div className="flex items-center gap-3">
                        <Avatar className="h-9 w-9">
                          <AvatarFallback className="bg-primary/20 text-primary text-sm">
                            {client.name
                              .split(" ")
                              .map((n) => n[0])
                              .join("")}
                          </AvatarFallback>
                        </Avatar>
                        <span className="font-medium text-foreground">
                          {client.name}
                        </span>
                      </div>
                    </TableCell>
                    <TableCell>
                      <div className="flex flex-col gap-1">
                        <div className="flex items-center gap-1 text-sm text-muted-foreground">
                          <Phone className="size-3" />
                          {client.phone}
                        </div>
                        <div className="flex items-center gap-1 text-sm text-muted-foreground">
                          <Mail className="size-3" />
                          {client.email}
                        </div>
                      </div>
                    </TableCell>
                    <TableCell>
                      <span
                        className={`font-medium ${
                          client.totalDebt > 0 ? "text-destructive" : "text-muted-foreground"
                        }`}
                      >
                        {client.totalDebt > 0 ? formatCurrency(client.totalDebt) : "-"}
                      </span>
                    </TableCell>
                    <TableCell>
                      <span className="text-success font-medium">
                        {formatCurrency(client.totalPaid)}
                      </span>
                    </TableCell>
                    <TableCell>{getStatusBadge(client.status)}</TableCell>
                    <TableCell className="text-muted-foreground">
                      {formatDate(client.lastPayment)}
                    </TableCell>
                    <TableCell>
                      <DropdownMenu>
                        <DropdownMenuTrigger asChild>
                          <Button variant="ghost" size="icon" className="size-8">
                            <MoreHorizontal className="size-4" />
                          </Button>
                        </DropdownMenuTrigger>
                        <DropdownMenuContent align="end">
                          <DropdownMenuItem>
                            <Eye className="mr-2 size-4" />
                            Ver detalle
                          </DropdownMenuItem>
                          <DropdownMenuItem>
                            <Pencil className="mr-2 size-4" />
                            Editar
                          </DropdownMenuItem>
                          <DropdownMenuItem>
                            <MessageSquare className="mr-2 size-4" />
                            Enviar WhatsApp
                          </DropdownMenuItem>
                          <DropdownMenuSeparator />
                          <DropdownMenuItem className="text-destructive">
                            <Trash2 className="mr-2 size-4" />
                            Eliminar
                          </DropdownMenuItem>
                        </DropdownMenuContent>
                      </DropdownMenu>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </motion.div>

      {/* Pagination info */}
      <motion.div variants={item} className="flex items-center justify-between text-sm text-muted-foreground">
        <span>
          Mostrando {filteredClients.length} de {clients.length} clientes
        </span>
      </motion.div>
    </motion.div>
  )
}
