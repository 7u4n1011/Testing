# ui_personas.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import personas  # importamos el módulo completo para usar sus funciones

def on_agregar():
    nombre = ent_nombre.get()
    apellido = ent_apellido.get()
    fecha = ent_fecha.get()
    peso = ent_peso.get()
    altura = ent_altura.get()

    # Intentamos convertir numéricos
    try:
        peso = float(peso)
        altura = float(altura)
    except ValueError:
        messagebox.showerror("Dato inválido", "Peso y altura deben ser números (usar punto para decimales).")
        return

    try:
        p = personas.crear_persona(nombre, apellido, fecha, peso, altura)
    except Exception as e:
        messagebox.showerror("Error de validación", str(e))
        return

    # Limpiar campos
    ent_nombre.delete(0, tk.END)
    ent_apellido.delete(0, tk.END)
    ent_fecha.delete(0, tk.END)
    ent_peso.delete(0, tk.END)
    ent_altura.delete(0, tk.END)
    lbl_edad_valor.config(text="--")

    refrescar_tabla()
    messagebox.showinfo("OK", f"Persona agregada.\nIMC: {p['imc']}  |  Edad (calculada): {p['edad']}")

def refrescar_tabla():
    # Vaciar
    for row in tabla.get_children():
        tabla.delete(row)
    # Llenar desde PERSONAS
    for idx, p in enumerate(personas.PERSONAS, start=1):
        tabla.insert(
            "", tk.END,
            values=(
                idx,
                p["nombre"],
                p["apellido"],
                p["fecha_nacimiento"].isoformat(),
                p["edad"],
                p["peso_kg"],
                p["altura_m"],
                p["imc"],
            )
        )

def on_limpiar_lista():
    if messagebox.askyesno("Confirmar", "¿Borrar todas las personas cargadas?"):
        personas.limpiar_personas()
        refrescar_tabla()

def on_fecha_focus_out(event=None):
    """
    Cuando el usuario sale del campo fecha, intentamos mostrar la edad calculada
    (usando la función con BUG intencional). Si la fecha es inválida, mostramos "??".
    """
    fecha_txt = ent_fecha.get().strip()
    if not fecha_txt:
        lbl_edad_valor.config(text="--")
        return

    # Validamos formato primero (sin popups)
    try:
        fecha = datetime.strptime(fecha_txt, "%Y-%m-%d").date()
    except ValueError:
        lbl_edad_valor.config(text="??")
        return

    # Calculamos edad usando la función con el bug
    try:
        edad = personas.calcular_edad(fecha)
        lbl_edad_valor.config(text=str(edad))
    except Exception:
        lbl_edad_valor.config(text="??")

# --- Ventana ---
root = tk.Tk()
root.title("Registro de Personas + IMC (Testing)")

# --- Formulario ---
frm_form = ttk.Frame(root, padding=12)
frm_form.grid(row=0, column=0, sticky="nsew")

ttk.Label(frm_form, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
ent_nombre = ttk.Entry(frm_form, width=22)
ent_nombre.grid(row=0, column=1, sticky="w")

ttk.Label(frm_form, text="Apellido:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
ent_apellido = ttk.Entry(frm_form, width=22)
ent_apellido.grid(row=1, column=1, sticky="w")

ttk.Label(frm_form, text="Fecha nac. (YYYY-MM-DD):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
ent_fecha = ttk.Entry(frm_form, width=22)
ent_fecha.grid(row=2, column=1, sticky="w")
ent_fecha.bind("<FocusOut>", on_fecha_focus_out)

# Label de edad al lado de la fecha
ttk.Label(frm_form, text="Edad:").grid(row=2, column=2, sticky="e", padx=8)
lbl_edad_valor = ttk.Label(frm_form, text="--", width=6, anchor="center")
lbl_edad_valor.grid(row=2, column=3, sticky="w")

ttk.Label(frm_form, text="Peso (kg):").grid(row=3, column=0, sticky="e", padx=5, pady=5)
ent_peso = ttk.Entry(frm_form, width=22)
ent_peso.grid(row=3, column=1, sticky="w")

ttk.Label(frm_form, text="Altura (m):").grid(row=4, column=0, sticky="e", padx=5, pady=5)
ent_altura = ttk.Entry(frm_form, width=22)
ent_altura.grid(row=4, column=1, sticky="w")

btn_agregar = ttk.Button(frm_form, text="Agregar persona", command=on_agregar)
btn_agregar.grid(row=5, column=0, columnspan=2, pady=10)

btn_limpiar = ttk.Button(frm_form, text="Limpiar lista", command=on_limpiar_lista)
btn_limpiar.grid(row=6, column=0, columnspan=2)

# --- Tabla ---
cols = ("#", "Nombre", "Apellido", "Fecha nac.", "Edad", "Peso (kg)", "Altura (m)", "IMC")
tabla = ttk.Treeview(root, columns=cols, show="headings", height=10)
for c in cols:
    tabla.heading(c, text=c)
    tabla.column(c, anchor="center", stretch=True, width=110)
tabla.grid(row=1, column=0, sticky="nsew", padx=12, pady=12)

# Scroll vertical
scroll_y = ttk.Scrollbar(root, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=1, column=1, sticky="ns")

# Layout expandible
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Precarga por si hay datos
refrescar_tabla()

root.mainloop()
